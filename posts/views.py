from django.shortcuts import render, redirect
from .models import Post, Comment
from accounts.models import Profile


def post_list(request): 
    posts = Post.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')
    print(posts)
    context = {
        'posts': posts,
        'comments': comments
    }
    if request.user != None:
        context.__setitem__('profile', Profile.objects.all().filter(user=request.user.id))
    return render(request, 'posts/post_list.html', context)


def post_create(request):
    return render(request, 'posts/post_form.html')