# Generated by Django 2.1.7 on 2019-03-21 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingridient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
    ]
