from django.forms import ModelForm
from django.db import models
from django import forms
from mGoal.models import *

class CofreForm(forms.ModelForm):
	
	class Meta:
		model = Cofre
		fields = ('valor_total', 'qtd_usuarios', 'nome_grupo', 'dt_meta', 'descricao')


class TransferenciaForm(forms.ModelForm):
	
	class Meta:
		model = Transacao
		fields = ('Destinatario', 'valor_transacao', 'data_transacao')


class UserForm(forms.ModelForm):
	
	class Meta:
		model = Usuario
		fields = ('nome', 'saldo')