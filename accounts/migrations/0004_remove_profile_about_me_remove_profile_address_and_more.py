# Generated by Django 4.0.3 on 2022-07-27 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_jop_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='about_me',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='jop_title',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
