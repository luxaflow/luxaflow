from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from .models import Profile, Experience, Education, Skill
from .forms import ProfileModelForm, ExperienceModelForm, EducationModelForm, SkillModelForm

def account_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = ProfileModelForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.user_img = form.cleaned_data['user_img']
            profile.save()
            return HttpResponseRedirect('/accounts/{0}/me'.format(user_id))
    else:
        form = ProfileModelForm(instance=profile)
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def experience_create(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        profile = get_object_or_404(Profile, user=user)
        form = ExperienceModelForm(request.POST or None)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.profile = profile
            experience.save()
            return HttpResponseRedirect('/accounts/{0}/experience'.format(user_id))
    else: 
        form = ExperienceModelForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def experience_edit(request, user_id, experience_id):
    experience = Experience.objects.get(id=experience_id)
    if request.method == 'POST':
        form = ExperienceModelForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/{0}/experience'.format(user_id))
    else:
        form = ExperienceModelForm(instance=experience)
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def experience_delete(request, user_id, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    if experience:
        experience.delete()
        return HttpResponseRedirect('/accounts/{0}/experience'.format(user_id))
    else:
        return HttpResponseRedirect('/accounts/{0}/experience'.format(user_id))


def education_create(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        profile = get_object_or_404(Profile, user=user)
        form = EducationModelForm(request.POST or None)
        if form.is_valid():
            education = form.save(commit=False)
            education.profile = profile
            education.save()
            return HttpResponseRedirect('/accounts/{0}/education'.format(user_id))
    else:
        form = EducationModelForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def education_edit(request, user_id, education_id):
    education = Education.objects.get(id=education_id)
    if request.method == 'POST':
        form = EducationModelForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/{0}/education'.format(user_id))
    else:
        form = EducationModelForm(instance=education)
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def education_delete(request, user_id, education_id):
    education = get_object_or_404(Education, id=education_id)
    if education:
        education.delete()
        return HttpResponseRedirect('/accounts/{0}/education'.format(user_id))
    else:
        return HttpResponseRedirect('/accounts/{0}/education'.format(user_id))


def skill_create(request, user_id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        profile = get_object_or_404(Profile, user=user)
        form = SkillModelForm(request.POST or None)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.profile = profile
            skill.save()
            return HttpResponseRedirect('/accounts/{0}/skill'.format(user_id))
    else:
        form = SkillModelForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def skill_edit(request, user_id, skill_id):
    skill = Skill.objects.get(id=skill_id)
    if request.method == 'POST':
        form = SkillModelForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/{0}/skill'.format(user_id))
    else:
        form = SkillModelForm(instance=skill)
        context = {
            'form': form
        }
        return render(request, 'accounts/account_form.html', context)


def skill_delete(request, user_id, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if skill:
        skill.delete()
        return HttpResponseRedirect('/accounts/{0}/skill'.format(user_id))
    else:
        return HttpResponseRedirect('/accounts/{0}/skill'.format(user_id))


def account_list(request, user_id):
    user = User.objects.get(id=user_id)
    profile = get_object_or_404(Profile, user=user)
    if 'experience' in request.path:
        list_group = Experience.objects.all().filter(profile=profile)
    elif 'education' in request.path:
        list_group = Education.objects.all().filter(profile=profile)
    elif 'skill' in request.path:
        list_group = Skill.objects.all().filter(profile=profile)
    context = {
        'list_group': list_group
    }
    return render(request, 'accounts/account_list.html', context)


