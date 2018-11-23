from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/<str:data_type>', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
