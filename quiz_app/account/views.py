# Django Imports
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Forms
from .forms import UserCreationForm, LogInForm, MediaForm

# Models
from .models import UserProfile
from quiz_select.models import Quiz

# Renders
def signup_render(request):
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            if User.objects.filter(email = email).exists():
                return render(request,'account/signup.html', {"ucreation": UserCreationForm, "error": "Email Already Exists!"})
            if User.objects.filter(username = username).exists():
                return render(request,'account/signup.html', {"ucreation": UserCreationForm, "error": "Username Already Exists!"})
            else:
                # saving user for login info
                user = User.objects.create_user(email=email, username=username, password=password)
                user.set_password(password)
                user.save()
                # creating a userprofile
                userp = UserProfile(email = email, username = username, password = password)
                userp.save()
                u = User.objects.get(email=email)
                user = authenticate(username=u.get_username(),password=password)
                login(request, user)
                return HttpResponseRedirect('/adminaccount')
    else:
        context = {
            "ucreation": UserCreationForm
        }
    return render(request, 'account/signup.html', context)

def login_render(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return render(request, "account/login.html", {'login': LogInForm})
    elif request.user.is_authenticated:
        return render(request, 'account/logout.html')

    context = {
        "login": LogInForm
    }
    return render(request, 'account/login.html', context)

@login_required(login_url='/login')
def logout_render(request):
    logout(request)
    return render(request, "account/login.html", {'login': LogInForm})

@login_required(login_url='/login')
def admin_render(request):
    if request.method == 'POST':
        event = Quiz(
            title = request.POST['title'],
            description = request.POST['desciption'],
            duration = request.POST['duration'],
            image_filepath = request.POST['image_filepath'],
            quiz_type = request.POST['quiz_type']
        )
        event.save()
    return render(request, "account/admin.html", {"event_form": MediaForm})


