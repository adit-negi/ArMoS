from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    problem_name = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    problem_img = models.ImageField(upload_to='images/')
