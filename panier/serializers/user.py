from rest_framework import serializers
from ..models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_type = serializers.ChoiceField(choices=User.STATUS, read_only=True)
    is_active = serializers.BooleanField(read_only=True)   
    class Meta:
        model= User
        fields = ('id','phone','lastName','firstName','password','email','adresse', 'user_type', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # return User.objects.create(**validated_data)
        user = User(
            phone=validated_data['phone'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            email=validated_data['email'],
            user_type=User.ADMIN,  # Set the user type to 'VENDEUR'
            adresse = validated_data['adresse']
        )
        # user.user_type='owner'
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# class VendeurUserSerializer(serializers.HyperlinkedModelSerializer):
#     user_type = serializers.ChoiceField(choices=User.STATUS, read_only=True)
#     is_active = serializers.BooleanField(read_only=True)   
#     class Meta:
#         model= User
#         fields = ('id','phone','lastName','firstName','password','email','adresse', 'user_type', 'is_active')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         # return User.objects.create(**validated_data)
#         user = User(
#             phone=validated_data['phone'],
#             firstName=validated_data['firstName'],
#             lastName=validated_data['lastName'],
#             email=validated_data['email'],
#             user_type=User.VENDEUR,  # Set the user type to 'VENDEUR'
#             adresse = validated_data['adresse']
#         )
#         # user.user_type='owner'
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
class BlockUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_active')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone', 'password')

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)