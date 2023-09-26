from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 


from .views import *



urlpatterns = [
    path('home', home, name='home'),
    path('categories', categoryList, name="categories"),
    path('add-category', addCategory, name="add-category"),
    path('update-category/<int:pk>', updateCategory, name="update-category"),
    path('delete-category/<int:pk>',  deleteCategory, name="delete-category"),

    path('articles',  articleList, name="articles"),
    path('add-article',  addArticle, name="add-article"),
    path('update-article/<int:pk>', updateArticle, name="update-article"),
    path('delete-article/<int:pk>',  deleteArticle, name="delete-article"),

    path('login',  loginPage, name="login"),
    path('logout',  logOutUser, name="logout"),

    path('commandes',  commandeList, name="commandes"),
] +  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 