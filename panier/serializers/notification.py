from rest_framework import serializers
from ..models.notification import Notification 
from ..serializers import OrderSerializer , UserSerializer

class NotificationsSerializer(serializers.ModelSerializer):
    order : OrderSerializer(read_only=True,source='order')
    user : UserSerializer(read_only=True,source='user')
    
    class Meta:
        model = Notification
        fields = '__all__'