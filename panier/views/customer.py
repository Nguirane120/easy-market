from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..serializers import CustumerSerializer
from ..models import Custumer


class CustumerAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/client/
    """
    queryset = Custumer.objects.all()
    serializer_class = CustumerSerializer

    def post(self, request, format=None):
        serializer = CustumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)
        
    def get(self, request, format=None):
        items = Custumer.objects.filter(archived=False).order_by('pk')
        serializer = CustumerSerializer(items, many=True)
        return Response(serializer.data)

class CustumerByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Custumer.objects.all()
    serializer_class = CustumerSerializer

    def get(self, request, id, format=None):
        try:
            item = Custumer.objects.filter(archived=False).get(pk=id)
            serializer = CustumerSerializer(item)
            return Response(serializer.data)
        except Custumer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)

    def put(self, request, id, format=None):
        try:
            item = Custumer.objects.filter(archived=False).get(pk=id)
        except Custumer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        self.data = request.data.copy()        
        serializer = CustumerSerializer(item, data= self.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Custumer.objects.filter(archived=False).get(id=kwargs["id"])
        except Custumer.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
                }, status=404)
        item.archived=True
        item.save()
        return Response({"message": "deleted"},status=204)