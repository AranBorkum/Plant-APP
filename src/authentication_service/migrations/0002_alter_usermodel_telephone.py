# Generated by Django 5.0.6 on 2024-06-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="telephone",
            field=models.CharField(max_length=20),
        ),
    ]
