from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('update_task/<int:pk>/', views.updateTask, name='update_task'),

    path('delete/<str:pk>/', views.deleteTask, name="delete"),

]
