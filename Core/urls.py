from django.contrib import admin
from django.urls import path, include
from . import views
from .forms import *

app_name = 'Core'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('InputAct/', views.input_activity),
    path('prj/', views.ProjectIndexView.as_view(), name='project_index'),
    path('prj/cr/', views.ProjectCreateView.as_view(), name='project_create'),
    path('prj/up/<slug:slug>', views.ProjectUpdateView.as_view(),
         name='project_update'),
    path('prj/del/<slug:slug>', views.ProjectDeleteView.as_view(),
         name='project_delete'),
    path('tsk/', views.TaskIndexView.as_view(), name='task_index'),
    path('tsk/<int:pk>', views.ProjectTaskDetailView.as_view(), name='task_detail'),
    path('tsk/cr/<int:ID_Project>',
         views.ProjectTaskCreateView.as_view(), name='task_create'),
    path('tsk/up/<int:pk>', views.ProjectTaskUpdateView.as_view(),
         name='task_update'),
    path('tsk/del/<int:pk>', views.ProjectTaskDeleteView.as_view(),
         name='task_delete'),

]
