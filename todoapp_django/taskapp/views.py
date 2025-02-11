from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Home Page - Display all tasks
def index(request):
    tasks = Task.objects.all()
    return render(request, 'content/home.html', {'tasks': tasks})

# Create Task Page
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        description = request.POST.get('description')

        if title and description:
            tasks =Task.objects.create(title=title, description=description, completed=False)
            tasks.save()
            return redirect('index')

    return render(request, 'content/create_task.html')

# Update Task Page
def update_task(request, task):
    task = get_object_or_404(Task, id=task.id)

    if request.method == 'POST':
        task.completed = not task.completed  # Toggle status
        task.save()
        return redirect('index')

    return render(request, 'content/update_task.html', {'task': task})


# Delete Task Page
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('index')

    return render(request, 'content/delete_task.html', {'task': task})
