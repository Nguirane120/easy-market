# Generated by Django 4.1.3 on 2023-07-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0004_alter_callbackpayment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('En cours de livraison', 'en cours de livraions'), ('En cours de traitement', 'en cours de traitement'), ('Livrée', 'livrée')], default='En cours de traitement', max_length=150),
        ),
    ]
