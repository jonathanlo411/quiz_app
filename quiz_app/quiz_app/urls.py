# Django imports
from django.contrib import admin
from django.urls import path

# Page routes
from landing.views import landing_render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_render, name="landing"),
]
