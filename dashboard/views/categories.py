from django.shortcuts import render, redirect
from panier.models import Category
from django.contrib import messages
from ..forms import CategorytForm
# Create your views here.

def categoryList(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'dashboard/categories/listCategory.html', context)


def addCategory(request):
    # Category_form = CategoryForm()
    if request.method == 'POST':
      categoryName = request.POST['categoryName']
      description = request.POST['description']
      images = request.POST['images']
      userId = request.user
      category = Category.objects.create(
          categoryName=categoryName,
          description=description,
          images=images,
          userId=userId
        )
      category.save()
          
      messages.info(request, 'Croduit ajoutee avec succes')
      return redirect('categories')
    # context = {'Category':Category}
    return render(request, 'dashboard/categories//ajoutCategory.html')


def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category_form = CategorytForm(instance=category)
    if request.method == 'POST':
        category_form = CategorytForm(request.POST, instance=Category)
        if category_form.is_valid():
            category_form.save()
            messages.info(request, 'Category modifiee avec succes')

            return redirect('categories')
    context = {'category_form':category_form}
    return render(request, 'dashboard/categories/updateCategory.html', context)


def deleteCategory(request, pk):
        category = Category.objects.get(id=pk)
        if request.method == "POST":
            category.delete()
            messages.info(request, 'category supprimee avec success')

            return redirect('categories')
        context = {"category":category}
        return render(request, 'dashboard/categories/deleteCategory.html', context)

