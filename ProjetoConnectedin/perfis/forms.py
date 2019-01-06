from django.forms import ModelForm
from perfis.models import Perfil
from django.db import models
from django import forms

class PostarForm(forms.Form):

	texto = forms.CharField(required=True)