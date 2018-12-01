from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Page, PageNotAnInteger, Paginator
from accounts.models import Profile, Experience, Education, Skill
from projects.models import Project
from posts.models import Post


def index(request):
    projects = Project.objects.filter(completed=False)[:4]
    posts = Post.objects.all().order_by('-created_at')[:4]
    context = {
        'projects': projects,
        'posts': posts,
    }
    return render(request, 'pages/index.html', context)


def about(request, data_type):
    profile = get_object_or_404(Profile, user__id=1)
    context = {
        'profile': profile,
    }
    if data_type == 'experience':
        experience = Experience.objects.all().filter(profile=profile).order_by('-from_date')
        paginator = Paginator(experience, 10)
        page = request.GET.get('page')
        paged_experience = paginator.get_page(page)
        context.__setitem__('data', paged_experience)
    elif data_type == 'education':
        education = Education.objects.all().filter(profile=profile).order_by('-from_date')
        paginator = Paginator(education, 10)
        page = request.GET.get('page')
        paged_education = paginator.get_page(page)
        context.__setitem__('data', paged_education)
    elif data_type == 'skill':
        data = Skill.objects.all().filter(profile=profile).order_by('-scale')
        context.__setitem__('language', data.filter(language=True))
        context.__setitem__('other', data.filter(other=True))
        context.__setitem__('framework', data.filter(framework=True))
        context.__setitem__('soft_skill', data.filter(soft_skill=True))
    return render(request, 'pages/about.html', context)


"""  ABOUT CONTENT AJAX REQUEST  """
def get_content(request, data_type, content_id):
    if data_type == 'experience':
        content = Experience.objects.filter(id=content_id)
    elif data_type == 'education':
        content = Education.objects.filter(id=content_id)
    elif data_type == 'skill':
        content = Skill.objects.filter(id=content_id)
    serialized_content = serializers.serialize('json', content)
    return JsonResponse(serialized_content, safe=False)