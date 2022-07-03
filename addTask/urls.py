from django.urls import path
from .views import TaskViews

urlpatterns = [
    path('todo-task/', TaskViews.as_view()),
    path('todo-task/<int:id>', TaskViews.as_view())
    
]