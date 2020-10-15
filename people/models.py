from django.db import models


class Person(models.Model):
    title = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    problem_descrition = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    problem_img = models.ImageField(upload_to='images/')
