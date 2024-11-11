from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todo

# Create your views here.
def todolist(request):
    todo_items = todo.objects.all()
    return render(request, 'todo.html', {'todo_items': todo_items})

def todo_post(request):
    todo_task = todo(content = request.POST["content"])
    letter_number = len(request.POST["content"])
    if letter_number > 0:
        todo_task.save()
    return HttpResponseRedirect("/todoapp/todo/")

def todo_delete(request, task_id):
    delete_task = todo.objects.get(id=task_id)
    delete_task.delete()
    return HttpResponseRedirect("/todoapp/todo/")

