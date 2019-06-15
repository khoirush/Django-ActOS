from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from Core.models import User, UserPersonnel, Personnel
from django.http import HttpResponse, HttpRequest


def landingPage(request):
    return render(request, "landingpage.html")


def login_page(request):
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return login_page(request)


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
    user = request.user
    if user is not None:
        obj_user = User.objects.get(username=user.username)
        obj_UserPerson = UserPersonnel.objects.get(ID_User=obj_user.id)
        idp = int(obj_UserPerson.ID_Personnel_id)
        obj_personnel = Personnel.objects.get(
            ID_Personnel=idp)
        context = {}
        context['fname'] = obj_personnel.First_Name
        context['lname'] = obj_personnel.Last_Name
        context['fullname'] = str(obj_personnel.First_Name) + \
            str(obj_personnel.Last_Name)
    return render(request, 'homepage.html', {'context': context})


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
