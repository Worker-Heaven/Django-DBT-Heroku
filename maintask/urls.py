from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/tasks/', views.tasks, name='task'),
]
