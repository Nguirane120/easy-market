
from rest_framework import serializers
from ..models import Category
from .user import UserSerializer
class CategorySerializer(serializers.ModelSerializer):
    vendeur = UserSerializer(read_only=True, source="vendeurId")
    # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    class Meta:
        model = Category
        fields =('id','categoryName','description','images','vendeurId','vendeur','archived')