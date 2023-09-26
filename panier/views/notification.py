from rest_framework import generics
from rest_framework.response import Response
# Assurez-vous que le chemin d'importation est correct
from ..models.notification import Notification
# Assurez-vous que le chemin d'importation est correct
from ..serializers.notification import NotificationsSerializer


class NotificationsApiView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer

    def post(self, request, format=None):
        serializer = NotificationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, format=None):
        items = Notification.objects.filter(archived=False)
        # Utilisez le sérialiseur, pas le modèle
        serializer = NotificationsSerializer(items, many=True)
        return Response(serializer.data)


class NotificationByIdApiView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationsSerializer

    def get(self, request, id, format=None):
        try:
            item = Notification.objects.filter(archived=False).get(pk=id)
            serializer = NotificationsSerializer(item)
            return Response(serializer.data)
        except Notification.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)


    def put(self, request, id, format=None):
        try:
            item = Notification.objects.filter(archived=False).get(pk=id)
        except Notification.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = NotificationsSerializer(
            item, data=self.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


    def delete(self, request, *args, **kwargs):
        try:
            item = Notification.objects.filter(
                archived=False).get(id=kwargs["id"])
        except Notification.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.archived = True
        item.save()
        return Response({"message": "deleted"}, status=204)
