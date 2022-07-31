# Generated by Django 4.0.6 on 2022-07-30 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_select', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quiz_type',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(default='null', max_length=400),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='image_filepath',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(default='null', max_length=50),
        ),
    ]
