from django import forms
from .models import Url

class UrlForm(forms.Form):
   
    texto_url = forms.CharField(required=True)
