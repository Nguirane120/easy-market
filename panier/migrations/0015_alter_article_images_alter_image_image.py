# Generated by Django 4.1.3 on 2023-08-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panier', '0014_image_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='panier.image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/article'),
        ),
    ]
