# Generated by Django 5.0.6 on 2024-06-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_service", "0002_remove_emaillogmodel_send_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="emaillogmodel",
            name="send_status",
            field=models.IntegerField(default=0),
        ),
    ]