from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo-list'),  
    path('todo/create/', views.create_todo, name='create-todo'),
    path('todo/<int:pk>/', views.todo_detail, name='todo-detail'),
]
