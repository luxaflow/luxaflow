from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import Profile, Experience, Education, Skill

class ProfileModelForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ('user', 'first_name', 'last_name', 'email',
                  'phone', 'mobile', 'about', 'user_img',)
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control', 'disabled': True}),
            'first_name': forms.TextInput(attrs={'class':  'form-control'}),
            'last_name': forms.TextInput(attrs={'class':  'form-control'}),
            'email': forms.TextInput(attrs={'class':  'form-control'}),
            'user_img': forms.FileInput(attrs={'class': 'form-control-file'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'user': _('Username:'),
            'first_name': _('First name:'),
            'last_name': _('Last name:'),
            'user_img': _('Profile image:'),
            'email': _('E-mail:'),
            'phone': _('Phone:'),
            'mobile': _('Mobile:'),
            'about': _('About Me:')
        }


class ExperienceModelForm(forms.ModelForm):
    class Meta():
        model = Experience
        fields = ('name', 'job_title','from_date', 'till_date', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'from_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'till_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        labels = {
            'name': _('Company:'),
            'job_title': _('Job Title:'),
            'from_date': _('From:'),
            'till_date': _('Till:'),
            'description': _('Description:')
        }


class EducationModelForm(forms.ModelForm):
    class Meta():
        model = Education
        fields = ('name', 'level', 'from_date', 'till_date', 'description', 'completed',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'from_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'till_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        labels = {
            'name': _('School:'),
            'level': _('Level:'),
            'from_date': _('From:'),
            'till_date': _('Till:'),
            'description': _('Description:'),
            'completed': _('Completed:')
        }


class SkillModelForm(forms.ModelForm):
    class Meta():
        model = Skill
        fields = ('name', 'scale', 'description', 'language', 'software', 'framework', 'soft_skill')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'scale': forms.NumberInput(attrs={'class': 'form-control', 'max': 5, 'min': 1}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'language': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'framework': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'software': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'soft_skill': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'name': _('Name:'),
            'scale': _('Scale:'),
            'description': _('Description:'),
            'language': _('Language:'),
            'software': _('Software:'),
            'framework': _('Framework:'),
            'sof_skill': _('Soft Skill:'),
        }
