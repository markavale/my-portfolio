# Generated by Django 3.1.1 on 2021-01-15 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_textmessage_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textmessage',
            name='duration',
        ),
        migrations.AddField(
            model_name='pagevisit',
            name='duration',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]