# Generated by Django 4.2.3 on 2023-09-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_seller_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_seller',
            field=models.BooleanField(default=False),
        ),
    ]
