# Generated by Django 2.2.3 on 2019-07-04 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='registered_dtt',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='writer',
        ),
    ]
