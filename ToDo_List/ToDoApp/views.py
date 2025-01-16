from django.shortcuts import render, redirect
from .models import ToDo
from django.views.decorators.http import require_POST

def index(request):
    todo_list = ToDo.objects.order_by('create_at')
    return render(request, 'ToDoApp/index.html', {'todo_list': todo_list})

@require_POST
def add_todo(request):
    title = request.POST['title']
    ToDo.objects.create(title=title)
    return redirect('index')

def toggle_todo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return redirect('index')
