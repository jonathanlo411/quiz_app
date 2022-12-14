# Django imports
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Page routes
from landing.views import landing_render
from quiz_select.views import movies_render, music_render, books_render
from quiz_picks.views import picks_render
from account.views import login_render, signup_render, admin_render, logout_render, delete_all_events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_render, name="landing"),
    path('movies', movies_render, name='movies_select'),
    path('music', music_render, name='music_select'),
    path('books', books_render, name='books_select'),
    path('picks', picks_render, name='picks'),
    path('login', login_render, name='login'),
    path('signup', signup_render, name='signup'),
    path('adminaccount', admin_render, name='admin'),
    path('logout_action', logout_render, name='logout'),
    path('delete_all_events', delete_all_events, name='delete_all_events')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


