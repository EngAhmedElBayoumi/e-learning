# Generated by Django 4.0.3 on 2022-07-26 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.EmailField(max_length=254)),
                ('Specialization', models.CharField(max_length=255)),
                ('Abstract', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/teams')),
                ('video', models.FileField(upload_to='videos_uploaded')),
            ],
        ),
    ]