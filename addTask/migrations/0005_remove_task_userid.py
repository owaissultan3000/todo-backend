# Generated by Django 4.0.4 on 2022-07-02 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addTask', '0004_task_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='userid',
        ),
    ]