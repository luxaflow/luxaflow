from accounts.models import Skill
from posts.models import Post
from projects.models import Project

def footer_data(request):
    footer_posts = Post.objects.all().order_by('-created_at')[:5]
    footer_skills = Skill.objects.filter(soft_skill=False).filter(software=False).order_by('-scale')[:5]
    footer_projects = Project.objects.all().order_by('-updated_at')[:5]
    return {'footer_posts': footer_posts, 'footer_skills': footer_skills, 'footer_projects': footer_projects}
