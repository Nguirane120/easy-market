# Generated by Django 3.2.21 on 2023-09-27 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0023_rename_createdby_acheteur_vendeurid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tailleur',
        ),
    ]