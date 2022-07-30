from django.shortcuts import render

# Create your views here.

def movies_render(request):
    return render(request, 'quiz_select/movies.html')

def music_render(request):
    return render(request, "quiz_select/music.html")

def books_render(request):
    return render(request, 'quiz_select/books.html')