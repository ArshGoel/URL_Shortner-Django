# Generated by Django 5.0.6 on 2024-05-19 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_url_clicks_delete_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]