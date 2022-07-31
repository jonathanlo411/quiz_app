from django.shortcuts import render

# Create your views here.

def signup_render(request):
    return render(request, 'account/signup.html')

def login_render(request):
    return render(request, 'account/login.html')