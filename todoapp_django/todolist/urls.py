from django.urls import path
from . import views

'''
To avoid namespace collision we add extra info about the
app such as app name
 '''

app_name = 'todolist'
urlpatterns = [
  path('',views.task1, name= "task" ),
  path('addtask/', views.addtask, name='add'),
  path('del/', views.deletetask, name= 'del'),
]