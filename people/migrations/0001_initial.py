# Generated by Django 3.0.2 on 2020-10-04 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('sneaker_name', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('shoe_img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
