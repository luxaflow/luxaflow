from django.shortcuts import render, get_object_or_404, HttpResponse
from accounts.models import Profile, Experience, Education, Skill
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
import json


def index(request):
    return render(request, 'public/index.html')


def about(request, data_type):
    user = get_object_or_404(User, id=1)
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile,
    }
    if data_type == 'me':
        data = profile.about
        context.__setitem__('data', data)
    elif data_type == 'experience':
        data = Experience.objects.all().filter(profile=profile).order_by('-from_date')
        context.__setitem__('data', data)
    elif data_type == 'education':
        data = Education.objects.all().filter(profile=profile).order_by('-from_date')
        context.__setitem__('data', data)
    elif data_type == 'skill':
        data = Skill.objects.all().filter(profile=profile).order_by('-scale')
        context.__setitem__('language', data.filter(language=True))
        context.__setitem__('software', data.filter(software=True))
        context.__setitem__('framework', data.filter(framework=True))
        context.__setitem__('soft_skill', data.filter(soft_skill=True))
    return render(request, 'public/about.html', context)


def dashboard(request):
    recent_action = LogEntry.objects.exclude(content_type__model='post').order_by('-action_time')[:10]
    print(type(recent_action))
    for item in recent_action:
        print(type(item))
    context = {
        'recent_action': recent_action
    }
    return render(request, 'dashboard.html', context)

