from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm,TaskUpdateForm


# Create your views here.


# ✅ Function to list all tasks

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

#view to create a new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
            form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})
    
#view to update an existing task
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch the task object

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:  
        form = TaskUpdateForm(instance=task)  # ✅ Use TaskUpdateForm, not TaskForm

    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})

#view to delete a task 
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task} )

