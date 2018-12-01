from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/<str:data_type>', views.about, name='about'),
    path('about/<str:data_type>/detail/<int:content_id>', views.get_content, name='get_content'),
]
