

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from todoapp.models import TODOAPP


def home(request):
    comp_task = TODOAPP.objects.filter(is_completed=False)
    finish_task = TODOAPP.objects.filter(is_completed=True)
    context = {
        'comp_task': comp_task,
        'finish_task': finish_task
    }
    return render(request, 'home.html', context)


def all(request):
    data = TODOAPP.objects.all().values(
        'task_name', 'is_completed', 'created_at', 'updated_at')
    return JsonResponse(list(data), safe=False)
