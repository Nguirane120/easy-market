from rest_framework import generics
from ..serializers import ImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from ..models import Image


class ImageAPIView(generics.ListCreateAPIView):
    """
    API endpoint pour gérer les images.
    """
    queryset = Image.objects.filter(archived=False)
    serializer_class = ImageSerializer
    # Permet de traiter les fichiers
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    # Vous pouvez ajouter des méthodes personnalisées ici si nécessaire

    def get(self, request, format=None):
        items = Image.objects.filter(archived=False).order_by('pk')
        serializer = ImageSerializer(items, many=True)
        return Response(serializer.data)


class ImageByAPIView(generics.RetrieveUpdateDestroyAPIView):

    """
    API endpoint pour gérer les details des images du produit , update , delete.
    """
    queryset = Image.objects.filter(archived=False)
    serializer_class = ImageSerializer
    
    def get(self, request, id , *args, **kwargs):
        try:
            item = Image.objects.filter(archived=False).get(pk=id)
            serializer = ImageSerializer(item)
            return Response(serializer.data)
        except Image.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
            
    def put(self, request, id, format=None):
        try:
            item = Image.objects.filter(archived=False).get(pk=id)
        except Image.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = ImageSerializer(item, data=self.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Image.objects.filter(archived=False).get(id=kwargs["id"])
        except Image.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.archived = True
        item.save()
        return Response({"message": "deleted"}, status=204)
    