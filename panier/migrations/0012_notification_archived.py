# Generated by Django 4.1.3 on 2023-08-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0011_rename_notificationsmodel_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
