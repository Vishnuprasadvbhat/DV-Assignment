from django.urls import path
from .views import home, create_task, update_task, delete_task

urlpatterns = [
    path('', home, name='home'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/update/<int:id>/', update_task, name='update_task'),
    path('tasks/delete/<int:id>/', delete_task, name='delete_task'),
]
