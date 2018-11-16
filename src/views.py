from django.shortcuts import render, get_object_or_404, HttpResponse
from accounts.models import Profile
from django.contrib.auth.models import User
import json

def index(request):
    return render(request, 'public/index.html')


def about(request, data_type):
    user = get_object_or_404(User, id=1)
    profile = get_object_or_404(Profile, user=user)

    if data_type == 'me':
        data = profile.about

    context = {
        'profile': profile,
        'data': data
    }
    return render(request, 'public/about.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


