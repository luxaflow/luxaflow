from django.shortcuts import render

def index(request):
    return render(request, 'public/index.html')


def dashboard(request):
    return render(request, 'dashboard.html')