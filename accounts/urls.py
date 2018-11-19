from django.urls import path
from . import views

urlpatterns = [
    path('', views.account_edit, name='account_edit'),
    path('experience', views.account_list, name='experience_list'),
    path('experience/create', views.experience_create, name='experience_create'),
    path('experience/<int:experience_id>/edit', views.experience_edit, name='experience_edit'),
    path('experience/<int:experience_id>/delete', views.experience_delete, name='experience_delete'),
    path('education', views.account_list, name='education_list'),
    path('education/create', views.education_create, name='education_create'),
    path('education/<int:education_id>/edit', views.education_edit, name='education_edit'),
    path('education/<int:education_id>/delete', views.education_delete, name='education_delete'),
    path('skill', views.account_list, name='skill_list'),
    path('skill/create', views.skill_create, name='skill_create'),
    path('skill/<int:skill_id>/edit', views.skill_edit, name='skill_edit'),
    path('skill/<int:skill_id>/delete', views.skill_delete, name='skill_delete'),
]
