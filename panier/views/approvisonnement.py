from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Article
from ..serializers import ArticleSerializer


class ApprovisonArticle(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = Article.objects.filter(archived=False).get(pk=id)
            serializer = ArticleSerializer(item)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)

    def put(self, request, id, format=None):

        try:
            item = Article.objects.filter(archived=False).get(id=id)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        serializer = ArticleSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            current_stock_quantity = item.articleInStock
            new_stock_quantity = request.data.get('articleInStock', current_stock_quantity)

            # Ajoutez la nouvelle quantité à la quantité actuelle en stock
            item.articleInStock = current_stock_quantity + new_stock_quantity
            item.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=400)