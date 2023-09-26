from rest_framework import serializers
from ..models import Acheteur
from .user import UserSerializer

class AcheteurSerialzer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source="createdBy")

    class Meta:
        model = Acheteur
        fields = ['id', 'phone', 'lastName', 'firstName', 'createdBy','user','password', 'email', 'adresse', 'is_active']
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Acheteur(
            phone=validated_data['phone'],
            lastName=validated_data['lastName'],
            firstName=validated_data['firstName'],
            email=validated_data.get("email"),
            adresse=validated_data['adresse'],
            createdBy=validated_data['createdBy'],
            user_type="ACHETEUR",
        )
        # Utilisez set_password pour crypter le mot de passe
        user.set_password(validated_data['password'])
        user.save()
        return user
