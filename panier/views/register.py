from rest_framework import generics, permissions, status
from django.db.models.functions import TruncDate, TruncMonth, TruncWeek
from ..serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from panier.models import *
from panier.serializers import *


# list user
class UserAPIView(generics.CreateAPIView):
    """
    GET api/v1/users/
    POST api/v1/users/
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.all().order_by("-date_joined")
        if not user:
            return Response(
                {
                    "status": "failure",
                    "message": "no such item",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UserSerializer(user, many=True)
        return Response(
            {
                "status": "success",
                "message": "user successfully retrieved.",
                "count": user.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        # user = request.data
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserById(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        try:
            item = User.objects.get(pk=pk)
            serializer = UserSerializer(item)

            articles = Article.objects.filter(userId=item)
            user_articles = ArticleSerializer(articles, many=True).data
            user_article_count = Article.objects.filter(userId=item).count()
            
            category = Category.objects.filter(userId=item)
            user_category = CategorySerializer(category,many=True).data
            user_category_count = Category.objects.filter(userId=item).count()
            commande = Order.objects.filter(userId=item)
            user_commande = OrderSerializer(commande, many=True).data
            user_commande_count = Order.objects.filter(userId=item).count()

            vente_par_jour = Order.objects.filter(userId=item).annotate(date=TruncDate('date_created')).values('date').annotate(total_sales=Sum('orderQuantity'))

            vente_par_mois = Order.objects.filter(userId=item).annotate(month=TruncMonth('date_created')).values('month').annotate(total_sales=Sum('orderQuantity'))

            vente_par_semaine = Order.objects.filter(userId=item).annotate(week=TruncWeek('date_created')).values('week').annotate(total_sales=Sum('orderQuantity'))

            return Response(
                {
                    "user_article_count": user_article_count,
                    "user_articles": user_articles,
                    "user_category_count": user_category_count,
                    "user_category": user_category,
                    "user_commande_count": user_commande_count,
                    "user_commande": user_commande,
                    "vente_par_jour":vente_par_jour,
                    "vente_par_mois":vente_par_mois,
                    "vente_par_semaine":vente_par_semaine,
                    "user": serializer.data,
                }
            )
        except Article.DoesNotExist:
            return Response(
                {
                    "status": "failure",
                    "message": "no such item with this id",
                },
                status=404,
            )

    def put(self, request, id, format=None):
        try:
            item = User.objects.filter(archived=False).get(id=id)
        except User.DoesNotExist:
            return Response(
                {
                    "status": "failure",
                    "message": "no such item with this id",
                },
                status=404,
            )
        serializer = UserSerializer(item, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class UserUpdatePassword(generics.CreateAPIView):
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, id, format=None):
        try:
            item = User.objects.filter(archived=False).get(pk=id)
            password = request.data["password"]
            item.set_password(password)
            item.save()
        except User.DoesNotExist:
            return Response(
                {
                    "status": "failure",
                    "message": "no such item with this id",
                },
                status=404,
            )

        # serializer = UserSerializer(item, data=request.data, partial= True)
        # if serializer.is_valid(raise_exception=True):
        # serializer.save()
        # return Response(serializer.data)
        return Response("serializer.errors", status=200)


class BlockUserAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = BlockUserSerializer  # Ajouter cette ligne pour définir le sérialiseur
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id, is_active=True)
            # print(user)
            serializer = BlockUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "user deactivated", "data":serializer.data})
        except User.DoesNotExist:
            return Response({'error': 'User not found or not a seller.'}, status=status.HTTP_404_NOT_FOUND)


class DeblockUserAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = BlockUserSerializer  # Ajouter cette ligne pour définir le sérialiseur
    def put(self, request, user_id):
        try:
            user = User.objects.get(id=user_id, is_active=False)
            # print(user)
            serializer = BlockUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "user activated", "data":serializer.data})
        except User.DoesNotExist:
            return Response({'error': 'User not found or not a seller.'}, status=status.HTTP_404_NOT_FOUND)



# class AddUser(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = VendeurUserSerializer

#     def post(self, request):
#         # user = request.data
#         serializer = VendeurUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)