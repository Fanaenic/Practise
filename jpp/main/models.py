from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    url = models.URLField()
    source = models.CharField(max_length=50)

class Resume(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    desired_position = models.CharField(max_length=255)
    url = models.URLField()
    source = models.CharField(max_length=50)
