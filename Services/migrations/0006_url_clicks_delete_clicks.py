# Generated by Django 5.0.6 on 2024-05-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_remove_url_clicks_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Clicks',
        ),
    ]