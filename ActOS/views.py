from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from Core.models import User, UserPersonnel, Personnel, Project, ProjectTask
from django.http import HttpResponse, HttpRequest
from Core.forms import *
from django.utils import timezone


def landingPage(request):
    return render(request, "landingpage.html")


def login_page(request):
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return login_page(request)


def get_user_context(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        obj_user = User.objects.get(username=user.username)
        obj_UserPerson = UserPersonnel.objects.get(ID_User=obj_user.id)
        idp = int(obj_UserPerson.ID_Personnel_id)
        obj_personnel = Personnel.objects.get(
            ID_Personnel=idp)
        context = {}
        context['user'] = user
        context['id_personnel'] = obj_personnel
        context['fname'] = obj_personnel.First_Name
        context['lname'] = obj_personnel.Last_Name
        context['fullname'] = str(obj_personnel.First_Name) + \
            str(obj_personnel.Last_Name)
        projects = []
        assignment_list = ProjectAssignment.objects.all().filter(
            ID_Personnel=context['id_personnel'])
        list_id_project = []
        for asg in assignment_list.values('ID_Project'):
            list_id_project.append(asg['ID_Project'])
        if not request.user.is_superuser:
            projects.append(Project.objects.get(
                ID_Project__in=list_id_project))
        else:
            projects = Project.objects.all()
        project_tasks = {}
        progress = {}
        for p in projects:
            progress[p.ID_Project] = ProjectProgress(p.ID_Project)
            idx = p.ID_Project
            project_tasks[idx] = ProjectTask.objects.filter(ID_Project=idx)
        context['Progress'] = progress
        context['Projects'] = projects
        context['Tasks'] = project_tasks
    return context


def login_view(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        obj_user = User.objects.get(username=username)
        obj_UserPerson = UserPersonnel.objects.get(ID_User=obj_user.id)
        idp = int(obj_UserPerson.ID_Personnel_id)
        obj_personnel = Personnel.objects.get(
            ID_Personnel=idp)
        context = {}
        context['fname'] = obj_personnel.First_Name
        context['lname'] = obj_personnel.Last_Name
        context['fullname'] = str(obj_personnel.First_Name) + \
            str(obj_personnel.Last_Name)

        # Redirect to a success page.

        return redirect('/home/', {'context': context})
        # return HttpRequest(request, 'home/', {'obj': obj})
    else:
        # Return an 'invalid login' error message.
        return render(request, 'registration/login.html', {'errMessage': 'User Credentials Unknown'})


def home_page(request):
    context = get_user_context(request)
    if context:
        # get project object

        return render(request, 'homepage.html', context)
    # breakpoint()
    return login_page(request)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


class ProjectProgress():
    def __init__(self, ID_Project):
        self.ID_Project = ID_Project
        self.Progress = self.calculate_progress()

    def __str__(self):
        return str('%.2f' % self.Progress)

    def calculate_progress(self):
        prg = 0
        proj = Project.objects.get(ID_Project=self.ID_Project)
        total_weight = 0
        total_complete = 0
        for t in proj.task.all():
            total_weight += t.PctWeight
            total_complete += t.PctComplete * t.PctWeight / 100
        prg = total_complete / total_weight * 100
        return prg
