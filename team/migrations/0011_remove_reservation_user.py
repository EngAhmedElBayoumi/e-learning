# Generated by Django 4.0.3 on 2022-07-31 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_alter_reservation_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
    ]
