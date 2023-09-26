from django.db import models
# from django.db.models import Sum
# from django.db.models import Max
# from .customer import Custumer
from .article import Article
from .payment import CallbackPayment
from .user import User



class Order(models.Model):
    
    PAYMENT_CHOICES = (
        ('espece', 'Espèces'),
        ('wave', 'Wave'),
        ('orange_money', 'Orange Money')
    )
    
    STATUS = (
        ('En cours de livraison', 'en cours de livraions'),
        ('En cours de traitement', 'en cours de traitement'),
        ('Livrée', 'livrée')
    )
    
    STATUS_PAIEMENT = (
        ('Impayées' , 'impayées'),
        ('Payées' , 'Payées'),
    )
    
    order_number = models.CharField(max_length=100, unique=True, default='0000')
    date_created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1 , null=True)
    articleId = models.ManyToManyField(Article)
    orderQuantity = models.IntegerField(default=0)
    status = models.CharField(max_length=150, choices=STATUS, default='En cours de traitement')
    paymentId = models.ForeignKey(CallbackPayment, on_delete=models.CASCADE, null=True, blank=True)
    archived = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='espece')
    status_paiement = models.CharField(max_length=50 , choices=STATUS_PAIEMENT , default='Impayées')
    phone = models.CharField(max_length=40, blank=True)
    firstName = models.CharField(max_length=100, blank=True)
    lastName = models.CharField(max_length=100, blank=True)
    adresse = models.CharField(blank=True, max_length=255, null=True)

    def __str__(self):
        return f"{self.userId} - {self.status}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.order_number = Order.generate_unique_numero_commande()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_unique_numero_commande():
        last_order = Order.objects.order_by('-order_number').first()
        if last_order:
            last_numero = int(last_order.order_number)
            new_numero = str(last_numero + 1).zfill(4)
        else:
            new_numero = '0001'
        return new_numero