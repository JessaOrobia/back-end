# Generated by Django 5.2 on 2025-04-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
