from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
# Create your views here.

class NewTaskForm(forms.Form):
  task = forms.CharField(label='New task')
  
'''
The problem is if other user loads the same page, my tasks are visible to him
Here we need a seperate new task interface for each user, so whenever he uses this page he can have differnt interface 
But what if a user add some task and reloads, all details will be lost

To solve this we use sessions in the django, it remembers you everytime you use the page, so helps to retrive as well as 
use saved details
'''


def task1(request):
  if "tasks" not in request.session:
      request.session['tasks'] = []
  return render(request, 'content/task1.html',{'tasks' : request.session['tasks']})


# alternative method of creating form
def addtask(request):
  if request.method == "POST":
    form = NewTaskForm(request.POST)
    if form.is_valid():
      newtask = form.cleaned_data['task']
      request.session['tasks'] += [newtask]
      return HttpResponseRedirect(reverse("todolist:task"))
    else:
      return render(request, 'content/addtask.html', {"form" : form})

  return render(request, "content/addtask.html",{'form' : NewTaskForm()})

    
def deletetask(request):
  if request.method == "POST":
    form = NewTaskForm(request.POST)
    if form.is_valid():
      newtask = form.cleaned_data['task']
      request.session['tasks'] -= [newtask]
      return HttpResponseRedirect(reverse("todolist:del"))
    else:
      return render(request, 'content/task1.html', {
        "form" : form
      })

  return render(request, "content/task1.html",{'form' : NewTaskForm()})