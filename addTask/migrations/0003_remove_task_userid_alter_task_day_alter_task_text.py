# Generated by Django 4.0.4 on 2022-07-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addTask', '0002_task_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='userid',
        ),
        migrations.AlterField(
            model_name='task',
            name='day',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
