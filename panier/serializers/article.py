
from rest_framework import serializers
from ..models import Article
from .category import CategorySerializer
from .user import UserSerializer
from .images import ImageSerializer


# class ArticleSerializer(serializers.ModelSerializer):
#     category = CategorySerializer(read_only=True, source="categoryId")
#     user = UserSerializer(read_only=True, source="userId")
#     # user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
#     class Meta:
#         model = Article
#         fields =('id','articleName','articleDescription','articlePrice','images','articleActif','articleInStock','categoryId','category','userId','user','archived' , 'isFavorite')

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, source="categoryId")
    vendeur = UserSerializer(read_only=True, source="vendeurId")
    imagesData = ImageSerializer(read_only=True, source="images", many=True)

    class Meta:
        model = Article
        fields = ('id', 'articleName', 'articleDescription', 'articlePrice', 'images', 'imagesData',
                  'articleActif', 'articleInStock','articleInStockSecurite', 'categoryId', 'category', 'vendeurId', 'vendeur', 'archived', 'isFavorite')
