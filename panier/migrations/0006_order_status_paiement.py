# Generated by Django 4.1.3 on 2023-07-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_paiement',
            field=models.CharField(choices=[('Impayées', 'impayées'), ('Payées', 'Payées')], default='Impayées', max_length=50),
        ),
    ]
