# Generated by Django 4.2 on 2023-04-18 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
