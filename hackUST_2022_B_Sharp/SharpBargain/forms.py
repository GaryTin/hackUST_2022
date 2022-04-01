from django import forms
from .models import *

class add_img_form(forms.ModelForm):
    class Meta:
        model = DB_Product
        fields = ['prod_type','prod_img']
        widgets = {
            'prod_type': forms.HiddenInput(),
        }