from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import AcheteurSerialzer, UserSerializer
from ..models import Acheteur, User


class CreateAcheteurAPIView(generics.CreateAPIView):
    """
    POST api/v1/client/
    """
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerialzer

    def post(self, request, format=None):
        serializer = AcheteurSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    
class AcheteurAllAPIView(generics.ListAPIView):
    """
    GET ALL api/v1/client/
    """
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerialzer

    def get(self, request, format=None):
        items = Acheteur.objects.filter(archived=False).order_by('pk')
        serializer = AcheteurSerialzer(items, many=True)
        return Response(serializer.data)
    
class AcheteurByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerialzer

    def get(self, request, id, format=None):
        try:
            item = Acheteur.objects.filter(archived=False).get(pk=id)
            serializer = AcheteurSerialzer(item)
            return Response(serializer.data)
        except Acheteur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = User.objects.filter(archived=False).get(pk=id)
        except Acheteur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = UserSerializer(item, data=self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Acheteur.objects.filter(archived=False).get(id=kwargs["id"])
        except Acheteur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "pas d'acheteur avec cet id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)
    
class RetreiveAcheteurByVendeurAPIView(generics.RetrieveAPIView):
   
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerialzer

    def get(self, request, id, format=None):
        try:
            items = Acheteur.objects.filter(archived=False).filter(vendeur_id=id)
            serializer = AcheteurSerialzer(items,many=True)
            return Response(serializer.data)
        except Acheteur.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)