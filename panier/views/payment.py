from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ..serializers import PaymentSerializer, OrderSerializer
from ..models import CallbackPayment, Order, User, Article
import json
from rest_framework import status
from rest_framework.response import Response
import hashlib


class CallbackAchatAPIView(generics.CreateAPIView):

    permission_classes = ()
    queryset = CallbackPayment.objects.all()
    serializer_class = PaymentSerializer

    def post(self, request, format=None):
        data = request.data
        new_status_paiement = data.get('status')

        if new_status_paiement == "SUCCESS":
            transaction = data.get('transaction')
            status_paiement = transaction['data']['data']['status_paiement']
            orderQuantity = transaction['data']['data']['orderQuantity']
            articleId = transaction['data']['data']['articleId']
            payment_method = transaction['data']['data']['payment_method']
            phone = transaction['data']['data']['phone']
            firstName = transaction['data']['data']['firstName']
            lastName = transaction['data']['data']['lastName']
            adresse = transaction['data']['data']['adresse']
            userId = transaction['data']['data']['userId']
            status_commande = transaction['data']['data']['status']

            # user_id = userId.get('userId')

            # if userId is not None:
            #     user = User.objects.get(id=userId)

            #     order = Order.objects.create(
            #         status_paiement=status_paiement,
            #         orderQuantity=orderQuantity,
            #         payment_method=payment_method,
            #         phone=phone,
            #         firstName=firstName,
            #         lastName=lastName,
            #         adresse=adresse,
            #         userId=user,
            #         status=status_commande
            #     )
            # else:
            #     # Si userId est null, vous pouvez gérer ce cas en fonction de vos besoins,
            #     # par exemple, créer la commande sans l'utilisateur associé.
            #     order = Order.objects.create(
            #         status_paiement=status_paiement,
            #         orderQuantity=orderQuantity,
            #         payment_method=payment_method,
            #         phone=phone,
            #         firstName=firstName,
            #         lastName=lastName,
            #         adresse=adresse,
            #         status=status_commande
            #     )

            # order.articleId.set(articleId)

            try:

                # Vous n'avez pas besoin de rechercher la commande après la création, car elle est déjà créée.
                # Vous pouvez maintenant retourner une réponse réussie.
                if userId is not None:
                    user = User.objects.get(id=userId)

                    order = Order.objects.create(
                        status_paiement=status_paiement,
                        orderQuantity=orderQuantity,
                        payment_method=payment_method,
                        phone=phone,
                        firstName=firstName,
                        lastName=lastName,
                        adresse=adresse,
                        userId=user,
                        status=status_commande
                    )
                else:
                    # Si userId est null, vous pouvez gérer ce cas en fonction de vos besoins,
                    # par exemple, créer la commande sans l'utilisateur associé.
                    order = Order.objects.create(
                        status_paiement=status_paiement,
                        orderQuantity=orderQuantity,
                        payment_method=payment_method,
                        phone=phone,
                        firstName=firstName,
                        lastName=lastName,
                        adresse=adresse,
                        status=status_commande
                    )

                order.articleId.set(articleId)
                return Response({'message': 'Commande créée avec succès.'}, status=201)
            except User.DoesNotExist:
                return Response({'message': 'L\'utilisateur associé à cet ID n\'existe pas.'}, status=400)
            except Exception as e:
                # Gérez les erreurs ici, par exemple, si la création de la commande échoue pour une raison quelconque.
                return Response({'message': 'Une erreur s\'est produite lors de la création de la commande.'}, status=400)
        else:
            CallbackPayment.objects.create(data={'status': False})
            return Response({"message": "Statut de paiement n'est pas SUCCESS."}, status=400)


# from rest_framework import generics
# from rest_framework.response import Response


# class CallbackAchatAPIView(generics.CreateAPIView):

#     permission_classes = ()
#     queryset = CallbackPayment.objects.all()
#     serializer_class = PaymentSerializer

#     def post(self, request, format=None):
#         data = request.data
#         new_status_paiement = data.get('status')

#         if new_status_paiement == "SUCCESS":
#             transaction = data.get('transaction')
#             # Assurez-vous que la structure des données transaction est correcte avant d'accéder à ses éléments.
#             if 'data' in transaction and 'data' in transaction['data']:
#                 transaction_data = transaction['data']['data']

#                 try:
#                     # Créez une nouvelle commande en utilisant la méthode .create()
#                     print(transaction_data)
#                     user_id = transaction_data.get('userId')
#                     user = User.objects.get(id=user_id)
#                     order = Order.objects.create(
#                         status_paiement=transaction_data.get(
#                             'status_paiement'),
#                         orderQuantity=transaction_data.get('orderQuantity'),
#                         # articleId=transaction_data.get('articleId'),
#                         payment_method=transaction_data.get('payment_method'),
#                         phone=transaction_data.get('phone'),
#                         firstName=transaction_data.get('firstName'),
#                         lastName=transaction_data.get('lastName'),
#                         adresse=transaction_data.get('adresse'),
#                         userId=user,
#                         status=transaction_data.get('status')
#                     )

#                     # Remplacez 'articles' par le nom correct
#                     articles = transaction_data.get('articles', [])
#                     order.articleId.set(articles)

#                     # Pas besoin de sauvegarder à nouveau la commande, car .create() l'a déjà fait.
#                     return Response({'message': 'Commande créée avec succès.'}, status=201)
#                 except Exception as e:
#                     # Gérez les erreurs ici, par exemple, si la création de la commande échoue pour une raison quelconque.
#                     return Response({'message': 'Une erreur s\'est produite lors de la création de la commande.'}, status=400)
#             else:
#                 return Response({'message': 'Structure de données transaction incorrecte.'}, status=400)
#         else:
#             # CallbackPayment.objects.create(data={'status': False})
#             return Response({"message": "Statut de paiement n'est pas SUCCESS."}, status=400)
