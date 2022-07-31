from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseNotFound

# Model
from quiz_select.models import Quiz

# Create your views here.

def picks_render(request):
    get_r = request.method == 'GET'
    if get_r and 'quiz_id' in request.GET:
        request_quiz_id = request.GET.get('quiz_id', None)
        quiz_obj = Quiz.objects.get(id=request_quiz_id)
        context = {
            "quiz": quiz_obj
        }
        return render(request, 'quiz_picks/picks.html', context)
    else:
        if not get_r:
            return HttpResponseForbidden("POST requests are forbidden.")
        elif not 'quiz_id' in request.GET:
            return HttpResponseNotFound("Quiz ID not specified")
        else:
            context = {
                "error": "Something went wrong..."
            }
            return render(request, 'quiz_picks/missing.html', context)