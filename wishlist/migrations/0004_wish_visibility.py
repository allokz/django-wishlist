# Generated by Django 3.2.7 on 2021-10-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0003_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='visibility',
            field=models.BooleanField(default='True'),
        ),
    ]