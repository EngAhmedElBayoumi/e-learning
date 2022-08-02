# Generated by Django 4.0.3 on 2022-07-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_teams_subject_alter_teams_abstract_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/teams/img', verbose_name=' الصورة الشخصية'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='video',
            field=models.FileField(blank=True, upload_to='static/teams/video', verbose_name=' فيديوا تعريفي'),
        ),
    ]