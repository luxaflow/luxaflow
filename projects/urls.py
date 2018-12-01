from django.urls import path
from . import views


urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('detail/<int:project_id>', views.get_project, name='get_project'),
]
