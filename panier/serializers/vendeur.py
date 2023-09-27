from rest_framework import serializers
from ..models import Vendeur
from .user import UserSerializer

class VendeurSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Vendeur
        fields = ['id', 'phone', 'lastName', 'firstName','password','user_type', 'email', 'adresse', 'is_active']
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Vendeur(
            phone=validated_data['phone'],
            lastName=validated_data['lastName'],
            firstName=validated_data['firstName'],
            email=validated_data.get("email"),
            adresse=validated_data['adresse'],
            user_type=validated_data['user_type'],
        )
        # Utilisez set_password pour crypter le mot de passe
        user.set_password(validated_data['password'])
        user.save()
        return user
