# Generated by Django 3.1.7 on 2021-04-01 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='Text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='Title',
            new_name='title',
        ),
    ]
