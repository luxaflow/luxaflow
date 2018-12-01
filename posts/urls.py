from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:post_id>', views.get_post, name='get_post'),
]
