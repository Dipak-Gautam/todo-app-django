

from django.shortcuts import render

from todoapp.models import TODOAPP


def home(request):
    comp_task = TODOAPP.objects.filter(is_completed=False)
    finish_task = TODOAPP.objects.filter(is_completed=True)
    context = {
        'comp_task': comp_task,
        'finish_task': finish_task
    }
    return render(request, 'home.html', context)
