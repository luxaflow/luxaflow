from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/me', views.account_edit, name='account_edit'),
    path('<int:user_id>/experience', views.account_list, name='experience_list'),
    path('<int:user_id>/experience/create', views.experience_create, name='experience_create'),
    path('<int:user_id>/experience/<int:experience_id>/edit', views.experience_edit, name='experience_edit'),
    path('<int:user_id>/experience/<int:experience_id>/delete', views.experience_delete, name='experience_delete'),
    path('<int:user_id>/education', views.account_list, name='education_list'),
    path('<int:user_id>/education/create', views.education_create, name='education_create'),
    path('<int:user_id>/education/<int:education_id>/edit', views.education_edit, name='education_edit'),
    path('<int:user_id>/education/<int:education_id>/delete', views.education_delete, name='education_delete'),
    path('<int:user_id>/skill', views.account_list, name='skill_list'),
    path('<int:user_id>/skill/create', views.skill_create, name='skill_create'),
    path('<int:user_id>/skill/<int:skill_id>/edit', views.skill_edit, name='skill_edit'),
    path('<int:user_id>/skill/<int:skill_id>/delete', views.skill_delete, name='skill_delete'),
]
