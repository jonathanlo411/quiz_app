# Django imports
from django.shortcuts import render

# Models
from .models import Quiz

# Renders
def movies_render(request):
    data = Quiz.objects.all().filter(quiz_type='movie')
    context = {
        "data": data
    }
    return render(request, 'quiz_select/movies.html', context)

def music_render(request):
    data = Quiz.objects.all().filter(quiz_type='music')
    context = {
        "data": data
    }
    return render(request, "quiz_select/music.html", context)

def books_render(request):
    data = Quiz.objects.all().filter(quiz_type='books')
    context = {
        "data": data
    }
    return render(request, 'quiz_select/books.html', context)