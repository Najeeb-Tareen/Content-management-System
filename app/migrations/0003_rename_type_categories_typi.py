# Generated by Django 5.0 on 2023-12-25 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='type',
            new_name='typi',
        ),
    ]