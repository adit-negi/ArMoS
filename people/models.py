from django.db import models

from geoposition.fields import GeopositionField
FRUIT_CHOICES = [
    ('Pitampura', 'Pitampura'),
    ('Karol Bagh', 'Karol Bagh'),
    ('Sadar Paharganj', 'Sadar Paharganj'),
    ('Civil Lines', 'Civil Lines'),
    ('Narela', 'Narela'),
    ('Rohini', 'Rohini'),
    ('Keshav Puram', 'Keshav Puram'),
    ('Central Delhi', 'Central Delhi'),
    ('South Delhi', 'South Delhi'),
    ('West Delhi', 'West Delhi'),
    ('Najafgarh', 'Najafgarh'),
    ('Shahdara South', 'Shahdara South'),
    ('Shahdara North', 'Shahdara North')
]


class Person(models.Model):
    title = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    problem_descrition = models.CharField(max_length=30, blank=False)
    location = models.CharField(
        max_length=30, blank=False, choices=FRUIT_CHOICES)
    problem_img = models.ImageField(upload_to='images/')


class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()
