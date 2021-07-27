from django import forms

from product.models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Product


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'