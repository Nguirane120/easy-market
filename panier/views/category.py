from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import CategorySerializer
from ..models import Category


class CategoryAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/category/
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Category.objects.filter(archived=False).order_by('pk')
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data)

class CategoryByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, id, format=None):
        try:
            item = Category.objects.filter(archived=False).get(pk=id)
            serializer = CategorySerializer(item)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Category.objects.filter(archived=False).get(pk=id)
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = CategorySerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Category.objects.filter(archived=False).get(id=kwargs["id"])
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
    


class CategoryVendeurIdView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, vendeurId, format=None):
        try:
            item = Category.objects.filter(archived=False, vendeurId=vendeurId)
            serializer = CategorySerializer(item, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "Cet item n'existe pas",
                }, status=404)