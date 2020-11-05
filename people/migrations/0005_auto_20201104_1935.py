# Generated by Django 2.2.8 on 2020-11-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_pointofinterest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.CharField(choices=[('Pitampura', 'Pitampura'), ('Karol Bagh', 'Karol Bagh'), ('Sadar Paharganj', 'Sadar Paharganj'), ('Civil Lines', 'Civil Lines'), ('Narela', 'Narela'), ('Rohini', 'Rohini'), ('Keshav Puram', 'Keshav Puram'), ('Central Delhi', 'Central Delhi'), ('South Delhi', 'South Delhi'), ('West Delhi', 'West Delhi'), ('Najafgarh', 'Najafgarh'), ('Shahdara South', 'Shahdara South'), ('Shahdara North', 'Shahdara North')], max_length=30),
        ),
    ]