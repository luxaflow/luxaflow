from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post


def post_list(request): 
    posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts,
    }
    print(str(paged_posts))
    return render(request, 'posts/post_list.html', context)


def get_post(request, post_id):
    serialized_post = serializers.serialize('json', Post.objects.filter(id=post_id))
    return JsonResponse(serialized_post, safe=False)
