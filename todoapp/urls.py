from django.urls import path
from . import views

urlpatterns = [
    path('complete/<int:pk>/', views.make_complete, name='make_complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('add_task/', views.add_task, name='add_task')
]
