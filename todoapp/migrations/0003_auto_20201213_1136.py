# Generated by Django 3.1.3 on 2020-12-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]