from django.http import HttpResponse
from django.shortcuts import redirect, render

from todoapp.models import TODOAPP

# Create your views here.


def make_complete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def delete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.delete()
    return redirect('home')


def add_task(request):
    task = request.POST['task']
    TODOAPP.objects.create(task_name=task)
    return redirect('home')
