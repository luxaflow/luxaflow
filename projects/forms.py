from django import forms
from .models import Project
from django.utils.translation import gettext_lazy as _


class ProjectModelForm(forms.ModelForm):
    class Meta():
        model = Project
        fields = (
            'name', 
            'git_repo', 
            'description', 
            'private', 
            'completed', 
            'main_img', 
            'img_1', 
            'img_2', 
            'img_3', 
            'img_4',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'git_repo': forms.URLInput(attrs={'class': 'form-control'}),
            'private': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'main_img': forms.FileInput(attrs={'class': 'form-control-file'}),
            'img_1': forms.FileInput(attrs={'class': 'form-control-file'}),
            'img_2': forms.FileInput(attrs={'class': 'form-control-file'}),
            'img_3': forms.FileInput(attrs={'class': 'form-control-file'}),
            'img_4': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'name': _('Name:'),
            'git_repo': _('Github Repository:'),
            'description': _('Description:'),
            'private': _('Private:'),
            'completed': _('Completed:'),
            'main_img': _('Main Image:'),
            'img_1': _('Image 1:'),
            'img_2': _('Image 2:'),
            'img_3': _('Image 3:'),
            'img_4': _('Image 4:'),
        }

