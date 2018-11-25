from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/<str:data_type>', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fetch_learing_detail/<int:id>', views.fetch_learning_detail, name='fetch_learning_detail'),
]
