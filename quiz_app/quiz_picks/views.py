from django.shortcuts import render

# Create your views here.

def picks_render(request):
    return render(request, 'quiz_picks/picks.html')