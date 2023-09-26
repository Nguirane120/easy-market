from panier.models import Category
from django import forms
from django.forms import ModelForm, TextInput, NumberInput,FileInput, Select



class CategorytForm(ModelForm):
    class Meta:
        model = Category
        fields = ['categoryName', 'description', 'images', 'userId']
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
            'userId': Select(attrs={
                'class': "form-control", 
               
                }),
        }
