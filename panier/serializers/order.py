
from django.db.models import Sum, F, DecimalField
from rest_framework import serializers
from ..models import Order
from .payment import PaymentSerializer
from .user import UserSerializer
from .article import ArticleSerializer
from .vendeur import VendeurSerialzer
from .acheteur import AcheteurSerialzer


class OrderSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(read_only=True)
    payment = PaymentSerializer(read_only=True, source="paymentId")
    article = ArticleSerializer(read_only=True, source="articleId", many=True)
    vendeur = VendeurSerialzer(read_only=True, source="vendeur_id")
    acheteur = AcheteurSerialzer(read_only=True, source="acheteur_id")
    total_price = serializers.SerializerMethodField()
    def get_total_price(self, obj):
        # Calculer le prix total des produits commandés pour l'objet Order
        total_price = Order.objects.filter(id=obj.id).aggregate(
            total_price=Sum(F('articleId__articlePrice') * F('orderQuantity'), output_field=DecimalField())
        )['total_price']
        # total_price = 0
        return total_price
    
    class Meta:
        model = Order
        fields = ('id', 'order_number', 'date_created', 'orderQuantity','articleId', 'article', 'status','paymentId','payment', 'archived', 'vendeur_id', 'vendeur', 'acheteur_id','acheteur', 'total_price' , 'payment_method' , 'status_paiement' , 'phone' , 'firstName' , 'lastName' , 'adresse')
        
        
class CommandesParJourSerializer(serializers.Serializer):
    date_creation = serializers.DateField()
    total = serializers.IntegerField()
    commandes_du_jour = OrderSerializer(many=True)
        
        
        