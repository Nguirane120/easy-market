# Generated by Django 4.1.3 on 2023-07-05 23:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone', models.CharField(max_length=40, unique=True)),
                ('firstName', models.CharField(blank=True, max_length=100)),
                ('lastName', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('adresse', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('tailleur', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_type', models.CharField(blank=True, choices=[('ACHETEUR', 'ACHETEUR'), ('VENDEUR', 'VENDEUR')], max_length=20)),
                ('archived', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleName', models.CharField(blank=True, max_length=250, null=True)),
                ('articleDescription', models.CharField(blank=True, max_length=512, null=True)),
                ('articlePrice', models.FloatField()),
                ('articleActif', models.BooleanField(blank=True, default=False, null=True)),
                ('articleInStock', models.IntegerField()),
                ('images', models.FileField(blank=True, null=True, upload_to='uploads/article')),
                ('archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CallbackPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Custumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=150, null=True)),
                ('lastName', models.CharField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('adress', models.CharField(max_length=255, null=True)),
                ('birthday', models.DateField(default=datetime.datetime.now)),
                ('archived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('userId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PanierElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('aricleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panier.article')),
                ('panierId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panier.panier')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default='0000', max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('orderQuantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('En cours de livraison', 'en cours de livraions'), ('En cours de traitement', 'en cours de traitement'), ('Payee', 'payee'), ('Payee et Livree', 'payee et livree'), ('Livree', 'payee et livree')], default='encours', max_length=150)),
                ('archived', models.BooleanField(default=False)),
                ('articleId', models.ManyToManyField(to='panier.article')),
                ('paymentId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panier.callbackpayment')),
                ('userId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='uploads/categoriy')),
                ('archived', models.BooleanField(default=False)),
                ('userId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categoryId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='panier.category'),
        ),
        migrations.AddField(
            model_name='article',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
