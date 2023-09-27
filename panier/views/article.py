from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import ArticleSerializer
from ..models import Article


class ArticleAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/Article/
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Article.objects.filter(archived=False).order_by('pk')
        serializer = ArticleSerializer(items, many=True)
        return Response(serializer.data)


class ArticleByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
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
            item = Article.objects.filter(archived=False).get(pk=id)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = ArticleSerializer(item, data=self.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Article.objects.filter(archived=False).get(id=kwargs["id"])
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.archived = True
        item.save()
        return Response({"message": "deleted"}, status=204)


class ArticleVendeurIdView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = Article.objects.filter(archived=False, categoryId=id)
            serializer = ArticleSerializer(item, many=True)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "Cet item n'existe pas",
            }, status=404)


class ArticleFavoriteView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, format=None):
        try:
            item = Article.objects.filter(isFavorite=True)
            serializer = ArticleSerializer(item, many=True)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "Cet item n'existe pas",
            }, status=404)
class AllArticleVendeurIdView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, id, format=None):
        try:
            item = Article.objects.filter(archived=False, vendeurId=id)
            serializer = ArticleSerializer(item, many=True)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "Cet item n'existe pas",
            }, status=404)
