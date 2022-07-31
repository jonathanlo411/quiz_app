from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=50, default='null')
    description = models.CharField(max_length=400, default='null')
    duration = models.FloatField()
    image_filepath = models.CharField(max_length=100, default='null')
    quiz_type = models.CharField(max_length=30, default='null')