# Generated by Django 5.0.6 on 2024-06-07 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("email_service", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="emaillogmodel",
            name="send_status",
        ),
    ]
