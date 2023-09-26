from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import PanierSerializer
from ..models import Panier


class PanierAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/Panier/
    """
    # queryset = Panier.objects.all()
    serializer_class = PanierSerializer

    def post(self, request, format=None):
        serializer = PanierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Panier.objects.filter(archived=False).Panier_by('pk')
        serializer = PanierSerializer(items, many=True)
        return Response(serializer.data)

class PanierByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Panier.objects.all()
    serializer_class = PanierSerializer

    def get(self, request, id, format=None):
        try:
            item = Panier.objects.filter(archived=False).get(pk=id)
            serializer = PanierSerializer(item)
            return Response(serializer.data)
        except Panier.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Panier.objects.filter(archived=False).get(pk=id)
        except Panier.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = PanierSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Panier.objects.filter(archived=False).get(id=kwargs["id"])
        except Panier.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)