from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Page, PageNotAnInteger, Paginator
from .models import Project


def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects, 10)
    page = request.GET.get('page')
    paged_projects = paginator.get_page(page)
    context = {
        'projects': paged_projects
    }
    return render(request, 'projects/project_list.html', context)


def get_project(request, project_id):
    serialized_project = serializers.serialize('json', Project.objects.filter(id=project_id))
    return JsonResponse(serialized_project, safe=False)