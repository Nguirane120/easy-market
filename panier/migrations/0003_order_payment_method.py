# Generated by Django 4.1.3 on 2023-07-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('espece', 'Espèces'), ('wave', 'Wave'), ('orange_money', 'Orange Money')], default='espece', max_length=50),
        ),
    ]
