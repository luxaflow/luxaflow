from django.contrib.admin.models import LogEntry
from posts.models import Post

def footer_data(request):
    footer_posts = Post.objects.all().order_by('-created_at')[:5]
    updates_list = ['skill', 'education', 'experience', 'profile']
    footer_updates = LogEntry.objects.filter(content_type__model__in=updates_list).order_by('-action_time')[:5]
    return {'footer_posts': footer_posts, 'footer_updates': footer_updates}
