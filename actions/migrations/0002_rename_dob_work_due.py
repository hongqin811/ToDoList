# Generated by Django 3.2.5 on 2021-07-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='dob',
            new_name='due',
        ),
    ]
