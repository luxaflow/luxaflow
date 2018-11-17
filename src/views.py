from django.shortcuts import render, get_object_or_404, HttpResponse
from accounts.models import Profile, Experience, Education, Skill
from django.contrib.auth.models import User
import json

def index(request):
    return render(request, 'public/index.html')


def about(request, data_type):
    user = get_object_or_404(User, id=1)
    profile = get_object_or_404(Profile, user=user)

    if data_type == 'me':
        data = profile.about
    elif data_type == 'experience':
        data = Experience.objects.all().filter(profile=profile).order_by('-from_date')
    elif data_type == 'education':
        data = Education.objects.all().filter(profile=profile).order_by('-from_date')
    elif data_type == 'skill':
        data = Skill.objects.all().order_by('is_language')

    context = {
        'profile': profile,
        'data': data
    }
    return render(request, 'public/about.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


