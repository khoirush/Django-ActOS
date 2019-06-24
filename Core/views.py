from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, DeleteView,
                                  UpdateView)
from . import models
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import *
from ActOS import views
from django.urls import reverse_lazy

# Create your views here.


def home_page(request):

    return views.home_page(request)


def input_activity(request):
    link = 'forms/inputAct.html'
    if request.user.is_authenticated:
        # act_filter = ActivityLogFilter(request.GET, queryset=task)
        context = views.get_user_context(request)
        # context['filter'] = act_filter
        return add_model_form(request, ActivityLogForm, link, context)
    return home_page(request)


def add_model_form(request, model_form, template_link, contexts):
    if request.user.is_authenticated:
        obj_user = User.objects.get(username=request.user.username)
        obj_UserPerson = UserPersonnel.objects.get(ID_User=obj_user.id)
        idp = int(obj_UserPerson.ID_Personnel_id)
        obj_personnel = Personnel.objects.get(
            ID_Personnel=idp)
        context = {}
        context['fname'] = obj_personnel.First_Name
        context['lname'] = obj_personnel.Last_Name
        if request.method == "POST":
            form = model_form(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect('/')

        else:

            form = model_form()
            context['form'] = form
            # context['filter'] = contexts['filter']
            return render(request, template_link, context)
    return render(request, 'registration/login.html')


# -------------- CBV - class based views
class ProjectIndexView(TemplateView):
    template_name = 'Core/Project_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(views.get_user_context(self.request))

        # projects = Project.objects.all()
        # project_tasks = {}
        # for p in projects:
        #     idx = p.ID_Project
        #     project_tasks[idx] = ProjectTask.objects.filter(ID_Project=idx)
        # context['Projects'] = projects
        # context['Tasks'] = project_tasks

        # context[""] =
        return context


class ProjectCreateView(CreateView):
    # fields = ('Title', 'Description', 'Total_Mandays',
    #           'Start_Date', 'End_Date')
    model = Project
    form_class = ProjectForm


class ProjectUpdateView(UpdateView):
    fields = ('Title', 'Description', 'Total_Mandays',
              'Start_Date', 'End_Date')
    model = Project


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('Core:project_index')


class TaskIndexView(TemplateView):
    template_name = 'Core/projecttask_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(views.get_user_context(self.request))

        # projects = Project.objects.all()
        # project_tasks = {}
        # progress = {}
        # for p in projects:
        #     progress[p.ID_Project] = ProjectProgress(p.ID_Project)
        #     idx = p.ID_Project
        #     project_tasks[idx] = ProjectTask.objects.filter(ID_Project=idx)
        # context['Projects'] = projects
        # context['Tasks'] = project_tasks
        # context['Progress'] = progress

        # context[""] =
        return context


class ProjectTaskDetailView(DetailView):
    model = ProjectTask
    template_name = 'Core/projecttask_detail.html'
    context_object_name = 'projecttask_detail'


class ProjectTaskCreateView(CreateView):
    # fields = ('Title', 'Description', 'Total_Mandays',
    #           'Start_Date', 'End_Date')
    model = ProjectTask
    form_class = ProjectTaskForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ID_Project = Project.objects.get(
            ID_Project=self.kwargs['ID_Project'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProjectTaskUpdateView(UpdateView):
    model = ProjectTask
    form_class = ProjectTaskForm


class ProjectTaskDeleteView(DeleteView):
    model = ProjectTask
    success_url = reverse_lazy('Core:task_index')

# --------------- PROJECT ASSIGNMENT


class AssignmentIndexView(TemplateView):
    template_name = 'Core/projectassignment_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(views.get_user_context(self.request))

        projects = context['Projects']
        assigned_personnel = {}
        for p in projects:
            try:
                assigned_personnel[p.ID_Project] = ProjectAssignment.objects.all().filter(
                    ID_Project=p.ID_Project)
            except:
                print('error when query data to project assignment')
        context['Projects'] = projects
        context['Assignment'] = assigned_personnel
        return context


class ProjectAssignmentDetailView(DetailView):
    model = ProjectAssignment
    template_name = 'Core/projectassignment_detail.html'
    context_object_name = 'projectassignment_detail'


class ProjectAssignmentCreateView(CreateView):
    # fields = ('Title', 'Description', 'Total_Mandays',
    #           'Start_Date', 'End_Date')
    model = ProjectAssignment
    form_class = ProjectAssignmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['Project'] = Project.objects.get(
                ID_Project=self.kwargs['pid'])
        except:
            print(
                f'Project Assignment Create : Error Retrieving Project where  ID_Project = {self.kwargs["pid"]}')
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.ID_Project = Project.objects.get(
            ID_Project=self.kwargs['pid'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# class ProjectAssignmentUpdateView(UpdateView):
#     model = ProjectAssignment
#     form_class = ProjectAssignmentForm

class ActivityLogIndexView(TemplateView):
    template_name = 'Core/activitylog_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(views.get_user_context(self.request))
        return context
