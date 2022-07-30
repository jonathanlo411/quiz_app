# Django imports
from django.contrib import admin
from django.urls import path

# Page routes
from landing.views import landing_render
from quiz_select.views import movies_render, music_render, books_render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_render, name="landing"),
    path('movies', movies_render, name='movies_select'),
    path('music', music_render, name='music_select'),
    path('books', books_render, name='books_select')
]
