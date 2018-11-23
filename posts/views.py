from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from accounts.models import Profile
from .forms import PostModelForm


def post_list(request): 
    posts = Post.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'comments': comments
    }
    return render(request, 'posts/post_list.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST or None)
        user = User.objects.get(id=request.user.id)
        profile = get_object_or_404(Profile, user=user)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('post_list')
    else:
        form = PostModelForm()
        context = {
            'form': form
        }
        return render(request, 'posts/post_form.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = PostModelForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'posts/post_form.html', context)


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post:
        post.delete()
        return redirect('post_list')