# Generated by Django 4.1.3 on 2023-08-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0013_image_remove_article_images_article_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
