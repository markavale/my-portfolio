# Generated by Django 3.1.1 on 2020-11-25 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20201125_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagevisit',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
