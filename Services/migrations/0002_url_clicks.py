# Generated by Django 5.0.6 on 2024-05-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]