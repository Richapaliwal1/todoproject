from django.urls import path
from . import views
from .views import TodoView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.TodoView, name='home'),
    path('create/', views.add_todo, name='add-todo'),
    path('read_all/', views.view_todo, name="read_all"),
    path('read_one/<str:pk>/', views.view_one, name="read_one"),
    path('update/<str:pk>/', views.todoUpdate, name="update"),
     path('delete/<str:pk>/', views.todoDelete, name="delete"),
]
