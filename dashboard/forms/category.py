from panier.models import Category
from django import forms
from django.forms import ModelForm, TextInput, NumberInput,FileInput, Select



class CategorytForm(ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName', 'description', 'images', 'vendeurId']
        widgets = {
            'categoryName': TextInput(attrs={
                'class': "form-control",
                # 'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'description': TextInput(attrs={
                'class': "form-control", 
                # 'style': 'max-width: 300px;',
                'placeholder': 'Quantite'
                }),
            'images': FileInput(attrs={
                'class': "form-control", 
               
                }),
            'vendeurId': Select(attrs={
                'class': "form-control", 
               
                }),
        }
