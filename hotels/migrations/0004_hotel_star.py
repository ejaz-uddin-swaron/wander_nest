# Generated by Django 5.1.3 on 2025-07-03 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_remove_hotel_image_hotel_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='star',
            field=models.IntegerField(default=1),
        ),
    ]
