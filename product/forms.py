from django import forms

from .models import ProductUpdate

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = ProductUpdate
        fields = "__all__"