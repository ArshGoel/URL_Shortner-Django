# Generated by Django 5.0.6 on 2024-05-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_clicks_remove_url_clicks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clicks',
        ),
        migrations.AddField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
