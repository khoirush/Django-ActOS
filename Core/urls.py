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
    path('prj/up/<int:pk>', views.ProjectUpdateView.as_view(), name='project_update'),
    path('prj/del/<int:pk>', views.ProjectDeleteView.as_view(),
         name='project_delete'),
]
