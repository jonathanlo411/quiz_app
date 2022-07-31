from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    email = models.EmailField(default="email@email.com")