
from rest_framework import serializers
from ..models import CallbackPayment
# from .Payment import PaymentSerializer


class PaymentSerializer(serializers.ModelSerializer):
    # Payment = PaymentSerializer(read_only=True, source="PaymentId")
    # user = UserSerializer(read_only=True)
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    class Meta:
        model = CallbackPayment
        fields = '__all__'