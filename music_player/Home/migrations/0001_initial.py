# Generated by Django 5.0.1 on 2024-01-24 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=100)),
                ('singer_image', models.FileField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs', models.FileField(upload_to='playlist/')),
                ('favourites', models.BooleanField(default=False)),
                ('singer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Home.music')),
            ],
        ),
    ]