# Generated by Django 3.2.15 on 2022-09-27 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='details',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]