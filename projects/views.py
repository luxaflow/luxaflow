from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectModelForm
from .models import Project


def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {
        'projects': projects
    }
    return render(request, 'projects/project_list.html', context)


def project_create(request):
    if request.method == 'POST':
        form = ProjectModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectModelForm()
        context = {
            'form': form
        }
        return render(request, 'projects/project_form.html', context)


def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ProjectModelForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            redirect('project_list')
    else:
        form =ProjectModelForm(instance=project)
        context = {
            'form': form,
            'project': project
        }
        return render(request, 'projects/project_form.html', context)


def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if project:
        project.delete()
        return redirect('request_list')
