from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import VendeurSerialzer
from ..models import Vendeur


class CreateVendeurAPIView(generics.CreateAPIView):
    """
    POST api/v1/client/
    """
    queryset = Vendeur.objects.all()
    serializer_class = VendeurSerialzer

    def post(self, request, format=None):
        serializer = VendeurSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

        
    
class VendeurAllAPIView(generics.ListAPIView):
    """
    GET ALL api/v1/vendeur/
    """
    queryset = Vendeur.objects.all()
    serializer_class = VendeurSerialzer

    def get(self, request, format=None):
        items = Vendeur.objects.filter(archived=False).order_by('pk')
        serializer = VendeurSerialzer(items, many=True)
        return Response(serializer.data)
    
class VendeurByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Vendeur.objects.all()
    serializer_class = VendeurSerialzer

    def get(self, request, id, format=None):
        try:
            item = Vendeur.objects.filter(archived=False).get(pk=id)
            serializer = VendeurSerialzer(item)
            return Response(serializer.data)
        except Vendeur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Vendeur.objects.filter(archived=False).get(pk=id)
        except Vendeur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = VendeurSerialzer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Vendeur.objects.filter(archived=False).get(id=kwargs["id"])
        except Vendeur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "pas vendeur avec cet id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
    
