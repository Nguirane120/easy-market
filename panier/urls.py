from django.urls import path, include
from django.conf import settings 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf.urls.static import static 
from . import views
from .views.notification import NotificationsApiView , NotificationByIdApiView

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Easy Market",
        default_version='1.0.0',
        description="Easy Market API documentation ",
    ),
    public=True,
)

urlpatterns = [
    path('v1/', 
        include([
            path('csrf/', views.GetCSRFToken.as_view()),
            # authentification 
            path('login/', views.LoginView.as_view()),
            path('logout/', views.logout_view),
            path('csrftoken', views.GetCSRFToken.as_view()),

            # path('reset-password/verify-token/', views.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
            # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

            # user 
            path('users/', views.UserAPIView.as_view()),
            path('users/<int:id>', views.UserById.as_view()),
            path('vendeur/block/<int:user_id>', views.BlockUserAPIView.as_view(), name='block_user'),
            path('vendeur/dblock/<int:user_id>', views.DeblockUserAPIView.as_view(), name='dblock_user'),
            # path('vendeur/', views.AddUser.as_view()),

            # path('user/password/<int:id>', views.UserUpdatePassword.as_view()),
            path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),

            # clients 
       
            path('clients',views.CustumerAPIView.as_view()),
            # path('clients/upload',views.CustomerUploadFileView.as_view()),
            # path('clients/export',views.CustomerExportFileView),
            path('clients/<int:id>/',views.CustumerByIdAPIView.as_view()),
            # path('clients/user/<int:id>/',views.CustomerByUser.as_view()),

            # commandes
            path('commandes/',views.OrderAPIView.as_view()),
            path('commandes/<int:id>/',views.OrderByIdAPIView.as_view()),
            path('commandes/bydate',views.FilterByDate.as_view()),
            path('commandes/bywave',views.OrderByWave.as_view()),
            path('commandes/numberorder',views.NumberOrderNoDelivered.as_view()),
            path('commandes/orderdelivered',views.OrderDelivered.as_view()),
            

            # commandes veundeur
            path('commandes/seller',views.OrderSellerAPIView.as_view()),
            path('commandes/seller/ordernodelivered',views.OrderSellerOrderNoDelivered.as_view()),
            path('commandes/seller/orderdelivered',views.OrderSellerDelivered.as_view()),
            


            # category 
            path('category/', views.CategoryAPIView.as_view()),
            path('category/<int:id>/', views.CategoryByIdAPIView.as_view()),
            path('category/user/<int:vendeurId>/',views.CategoryVendeurIdView.as_view()),


            # article 
            path('article/', views.ArticleAPIView.as_view()),
            path('article/<int:id>/', views.ArticleByIdAPIView.as_view()),
            path('articles/category/<int:id>/', views.ArticleVendeurIdView.as_view()),
            path('articles/vendeur/<int:id>/', views.AllArticleVendeurIdView.as_view()),
            path('article/favorite/' , views.ArticleFavoriteView.as_view()),

            path("approvison/<int:id>/",views.ApprovisonArticle.as_view()),

            # image article 
            path('images/', views.ImageAPIView.as_view()),
            path('images/<int:id>/', views.ImageByAPIView.as_view()),
            # path('images/' , views.ImageAPIView.as_view()),

            # #paiement
            path('paiement/', views.CallbackAchatAPIView.as_view()),
            # path('paiement/', views.PaymentAPIView.as_view()),
            # path('paiement/<int:pk>/', views.PaymentByIdAPIView.as_view()),
            # path('paiement/employee/<int:pk>/', getListPaimentByUser.as_view()),
            
            

            #panier
            # path('employees/', views.pani),
            # path('emplyees/', CreateEmployee.as_view()),
            # path('employees/<int:pk>', DetailEmployee.as_view()),
            
            
            #acheteur
            path('acheteurs/', views.AcheteurAllAPIView.as_view()),
            path('acheteur/', views.CreateAcheteurAPIView.as_view()),
            path('acheteur/<int:id>/', views.AcheteurByIdAPIView.as_view()),
            path('acheteurs/vendeur/<int:vendeurId>/', views.RetreiveAcheteurByVendeurAPIView.as_view()),

            # vendeur
             #acheteur
            path('vendeurs/', views.VendeurAllAPIView.as_view()),
            path('vendeur/', views.CreateVendeurAPIView.as_view()),
            path('vendeur/<int:id>/', views.VendeurByIdAPIView.as_view()),

            # Notification
            path('notifications/' , NotificationsApiView.as_view()),
            path('notifications/<int:id>/' , NotificationByIdApiView.as_view())

        ])
    ),
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 