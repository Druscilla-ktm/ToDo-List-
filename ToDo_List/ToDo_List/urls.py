"""
URL configuration for ToDo_List project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete'),
]
'''
from django.contrib import admin
from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('toggle/<int:todo_id>/', views.toggle_todo, name='toggle_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
]
'''
