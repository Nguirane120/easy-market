from django.shortcuts import render, redirect
from panier.models import Article, Category
from django.contrib import messages
from ..forms import ArticleForm
# Create your views here.

def articleList(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'dashboard/articles/listArticle.html', context)


def addArticle(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        articleName = request.POST['articleName']
        articleDescription = request.POST['articleDescription']
        articleInStock = request.POST['articleInStock']
        articlePrice = request.POST['articlePrice']
        categoryId = request.POST['categoryId']

        # Récupérer l'instance de Category correspondante
        category = Category.objects.get(id=categoryId)

        # Créer un nouvel objet Article avec les données du formulaire
        new_article = Article(
            articleName=articleName,
            articleDescription=articleDescription,
            articleInStock=articleInStock,
            articlePrice=articlePrice,
            categoryId=category  # Utiliser l'instance de Category
        )
        new_article.save()

        messages.info(request, 'Article ajouté avec succès')  # Message d'information

        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('articles')

    else:
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'dashboard/articles/ajoutArticle.html', context)


def updateArticle(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        Article_form = ArticleForm(request.POST, instance=article)
        if Article_form.is_valid():
            # Récupérer l'ID de l'article depuis la requête POST
            articleId = request.POST['articleId']
            # Vérifier que l'ID correspond à l'ID de l'article dans la base de données
            if int(articleId) == article.id:
                Article_form.save()
                messages.info(request, 'Article modifié avec succès')
                return redirect('articles')
            else:
                messages.error(request, 'Une erreur s\'est produite lors de la mise à jour de l\'article.')
    else:
        # Créer le formulaire avec l'instance de l'article
        Article_form = ArticleForm(instance=article)

    # Ajouter l'ID de l'article au contexte
    context = {'Article_form': Article_form, 'articleId': article.id}
    return render(request, 'dashboard/articles/updateArticle.html', context)




def deleteArticle(request, pk):
        article = Article.objects.get(id=pk)
        if request.method == "POST":
            article.delete()
            messages.info(request, 'Article supprimee avec success')

            return redirect('articles')
        context = {"article":article}
        return render(request, 'dashboard/articles/deleteArticle.html', context)

