from rest_framework import serializers
from ..models import Acheteur
from .user import UserSerializer

class AcheteurSerialzer(serializers.ModelSerializer):
    vendeur = UserSerializer(read_only=True, source="vendeurId")

    class Meta:
        model = Acheteur
        fields = ['id', 'phone', 'lastName', 'firstName', 'vendeur_id','password','user_type', 'email', 'adresse', 'is_active', 'vendeur']
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Acheteur(
            phone=validated_data['phone'],
            lastName=validated_data['lastName'],
            firstName=validated_data['firstName'],
            email=validated_data.get("email"),
            adresse=validated_data['adresse'],
            vendeur_id=validated_data['vendeur_id'],
            user_type=validated_data['user_type'],
        )
        # Utilisez set_password pour crypter le mot de passe
        user.set_password(validated_data['password'])
        user.save()
        return user
