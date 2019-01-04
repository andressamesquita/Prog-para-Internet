from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from perfis.models import Perfil
from usuarios.forms import *


class RegistrarUsuarioView(View):

	template_name = 'registrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		
		form = RegistrarUsuarioForm(request.POST)

		if form.is_valid():
			dados_form = form.cleaned_data

			usuario = User.objects.create_user(username = dados_form['nome'], email = dados_form['email'], password = dados_form['senha'])

			perfil = Perfil(nome=dados_form['nome'], telefone=dados_form['telefone'], 
				nome_empresa = dados_form['nome_empresa'], usuario = usuario)

			perfil.save()
			return redirect('index')


		return render(request, self.template_name, {'form':form})

class mudarSenhaView(View):

	template_name = 'mudar_senha.html'

	def get(self, request):
		form = AlterarSenhaForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		user = request.user
		form = AlterarSenhaForm(request.POST)
		
		if form.is_valid():
			form = form.cleaned_data
			if user.check_password(form['senha']):
				if form['nova_senha'] == form['confirma_senha']:
					print('i')
					user.set_password(form['nova_senha'])
					user.save()
					messages.success(request, 'Sua senha foi atualizada com sucesso!')
					return redirect('index')
			
			
			update_session_auth_hash(request, user)
			
			return redirect('mudar_senha')
		else:
			messages.error(request, 'Por favor, corrija o erro abaixo.')

		return render(request, 'mudar_senha.html', {'form': form}
)