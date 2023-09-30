from rest_framework import serializers
from ..models import User
from ..models import Vendeur

class VendeurSerialzer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=User.STATUS, read_only=True)

    class Meta:
        model = Vendeur
        fields = ['id', 'phone', 'lastName', 'firstName', 'password', 'email', 'adresse', 'is_active', 'raisonSocial', 'logo', 'region', 'ville', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Créez le vendeur en utilisant le modèle Vendeur lui-même
        vendeur = Vendeur(
            phone=validated_data['phone'],
            lastName=validated_data['lastName'],
            firstName=validated_data['firstName'],
            email=validated_data.get("email"),
            adresse=validated_data['adresse'],
            # raisonSocial=validated_data['raisonSocial'],
            # logo=validated_data['logo'],
           
            # ville=validated_data['ville'],
            user_type=User.VENDEUR,
            
        )
        # Utilisez set_password pour crypter le mot de passe
        vendeur.set_password(validated_data['password'])
        vendeur.save()
        return vendeur
