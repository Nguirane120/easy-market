from rest_framework import generics
from rest_framework.response import Response
from ..serializers import OrderSerializer, CommandesParJourSerializer
from ..models import Order,Article
import json
from django.shortcuts import get_object_or_404
from django.db.models import Count, F
from django.db.models.functions import TruncDate
from rest_framework import status
from ..models.notification import Notification
from rest_framework.pagination import PageNumberPagination
from kayjeund.pagination import CustomPageNumberPagination


def send_notification(sender, order):
    notification = Notification.objects.create(sender=sender, order=order)
    return notification


class OrderAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/order/
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # Create the order
            order = serializer.save()

            # Retrieve the articles included in the order
            article_ids = request.data.get('articleId', [])
            try:
                articles = Article.objects.filter(pk__in=article_ids)
            except Article.DoesNotExist:
                return Response({"message": "One or more articles do not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Reduce the available quantity for each article
            for article in articles:
                quantity = request.data['orderQuantity']  # You can adjust this based on your logic
                if article.articleInStock >= quantity:
                    article.articleInStock -= quantity
                    article.save()
                else:
                    return Response({
                        "status": "failure",
                        "message": f"Insufficient quantity available for article with ID {article.id}."
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        # Définissez la taille de la page à 10 ici.
        self.pagination_class.page_size = 10
        items = Order.objects.filter(
            archived=False).order_by('pk')
        # itemsNonLivre = Order.objects.filter(archived=False, userId=request.user.id).order_by('pk')
        paginated_items = self.paginate_queryset(items)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)


class NumberOrderNoDelivered(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):

        self.pagination_class.page_size = 10
        orderNoDelivered = Order.objects.filter(
            archived=False, userId=request.user.id).exclude(status='Livrée').order_by('pk')

        paginated_items = self.paginate_queryset(orderNoDelivered)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)


class OrderByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, id, format=None):
        try:
            item = Order.objects.filter(archived=False).get(pk=id)
            serializer = OrderSerializer(item)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
   
    def put(self, request, id, format=None):
        try:
            item = Order.objects.filter(archived=False).get(pk=id)
        except Order.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        self.data = request.data.copy()
        serializer = OrderSerializer(item, data=self.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, *args, **kwargs):
        try:
            item = Order.objects.filter(archived=False).get(id=kwargs["id"])
        except Order.DoesNotExist:
            return Response({
                "status": "failure",
                "message": "no such item with this id",
            }, status=404)
        item.archived = True
        item.save()
        return Response({"message": "deleted"}, status=204)


class FilterByDate(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = CommandesParJourSerializer
    pagination_class = CustomPageNumberPagination

    def get(self, request, format=None):
        self.pagination_class.page_size = 5
        commandes_par_jour = Order.objects.annotate(date_creation=TruncDate('date_created')).values(
            'date_creation').annotate(total=Count('id')).order_by('-date_creation')

        # Pagination des résultats
        paginated_commandes_par_jour = self.paginate_queryset(
            commandes_par_jour)

        resultats_serialises = []
        for info_commande in paginated_commandes_par_jour:
            date_creation = info_commande['date_creation']
            total_commandes = info_commande['total']
            commandes_du_jour = Order.objects.filter(
    date_created__date=date_creation).order_by('-order_number')


            resultats_serialises.append({
                'date_creation': date_creation,
                'total': total_commandes,
                'commandes_du_jour': commandes_du_jour,
            })

        serializer = CommandesParJourSerializer(
            resultats_serialises, many=True)

        # Utilisation de la réponse paginée
        return self.get_paginated_response(serializer.data)


class OrderByWave(generics.CreateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return Response({'response': 200})


class OrderDelivered(generics.RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        self.pagination_class.page_size = 10
        orderNoDelivered = Order.objects.filter(
            archived=False, userId=request.user.id, status="Livrée").order_by('pk')

        paginated_items = self.paginate_queryset(orderNoDelivered)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)


# ? VENDEUR VIEW
class OrderSellerAPIView(generics.ListCreateAPIView):
    """
    POST api/v1/order/
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            # orderId = order.id
            send_notification(sender=request.user, order=order)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        # Définissez la taille de la page à 10 ici.
        self.pagination_class.page_size = 10
        items = Order.objects.filter(
            archived=False).order_by('-pk')
        # itemsNonLivre = Order.objects.filter(archived=False, userId=request.user.id).order_by('pk')
        paginated_items = self.paginate_queryset(items)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)


class OrderSellerDelivered(generics.RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        self.pagination_class.page_size = 10
        orderNoDelivered = Order.objects.filter(
            archived=False, status_paiement="Payées").order_by('-pk')

        paginated_items = self.paginate_queryset(orderNoDelivered)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)


class OrderSellerOrderNoDelivered(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):

        self.pagination_class.page_size = 10
        orderNoDelivered = Order.objects.filter(
            archived=False).exclude(status='Livrée').order_by('-pk')

        paginated_items = self.paginate_queryset(orderNoDelivered)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)

class OrderByVendeur(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, id, format=None):
        self.pagination_class.page_size = 10
        id = self.kwargs.get('id')
        orders = Order.objects.filter(
            archived=False, vendeur_id=id)

        paginated_items = self.paginate_queryset(orders)
        serializer = OrderSerializer(paginated_items, many=True)
        return self.get_paginated_response(serializer.data)
