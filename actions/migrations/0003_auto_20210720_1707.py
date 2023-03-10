# Generated by Django 3.2.5 on 2021-07-20 21:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions', '0002_rename_dob_work_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='due',
            field=models.DateField(default=datetime.date(2021, 7, 20)),
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('due', models.DateField(default=datetime.date(2021, 7, 20))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
