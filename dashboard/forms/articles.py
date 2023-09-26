from panier.models import Article
from django import forms
from django.forms import ModelForm, TextInput, NumberInput,FileInput, Select



class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('articleName', 'articleDescription', 'articlePrice', 'articleInStock', 'categoryId', 'images', 'userId')
        widgets = {
            'articleName': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'articleDescription': TextInput(attrs={
                'class': "form-control", 
                # 'style': 'max-width: 300px;',
                'placeholder': 'Description'
                }),
            'articlePrice': NumberInput(attrs={
                'class': "form-control", 
               
                }),
            'articleInStock': NumberInput(attrs={
                'class': "form-control", 
                'placeholder': 'Quantite'
                }),
            'images': FileInput(attrs={
                'class': "form-control", 
               
                }),
            'categoryId': Select(attrs={
                'class': "form-control", 
               
                }),
            'userId': Select(attrs={
                'class': "form-control", 
               
                }),
        }
