# Generated by Django 3.2.7 on 2021-09-20 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_person_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
