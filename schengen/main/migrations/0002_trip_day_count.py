# Generated by Django 4.1.5 on 2023-01-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='day_count',
            field=models.IntegerField(default=0),
        ),
    ]
