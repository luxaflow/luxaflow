from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('name', 'body',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}) 
        }
        labels = {
            'name': _('Title:'),
            'body': _('Body:'),
        }


class CommentModelForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('body',) 
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),
        }