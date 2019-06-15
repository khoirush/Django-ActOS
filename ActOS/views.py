from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def landingPage(request):
    return render(request, "homepage.html")


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
        # Redirect to a success page.
        return render(request, 'homepage.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'registration/login.html', {'errMessage': 'User Credentials Unknown'})
