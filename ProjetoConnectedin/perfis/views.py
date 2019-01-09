from django.shortcuts import render, redirect
from perfis.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from perfis.forms import *


@login_required
def index(request):
	perfil_logado = get_perfil_logado(request)
	
	return render(request, 'index.html',{'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

@login_required
def perfil(request):
	
	perfil_logado = get_perfil_logado(request)
	usuarios_nao_bloqueados = perfil_logado.perfis_nao_bloqueados
	
	return render(request, 'perfil.html',{'perfis' : usuarios_nao_bloqueados, 
							'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	pode_convidar = perfil_logado.pode_convidar(perfil_id)
	pode_bloquear = perfil_logado.pode_bloquear(perfil)
	pode_mostrar = perfil_logado.mostrar_perfil(perfil)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request), 'pode_convidar': pode_convidar, 'pode_bloquear': pode_bloquear, 'mostrar_perfil': pode_mostrar})



@login_required
def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id) 
	perfil_logado = get_perfil_logado(request) 
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return redirect('index')

@login_required
def get_perfil_logado(request):

	return request.user.perfil

@login_required
def aceitar(request, convite_id):
	
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('perfil')

@login_required
def recusar(request, convite_id):
	
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('perfil')

@login_required
def desfazer_amizade(request, perfil_id):

	perfil_logado = get_perfil_logado(request)
	perfil_logado.desfazer_amizade(perfil_id)
	return redirect('perfil')

@login_required
def setar_super_user(self, perfil_id):
	
	perfil = Perfil.objects.get(id = perfil_id)
	perfil.setar_super_user()
	return redirect('perfil')


@login_required
def bloquear_perfil(request, perfil_id):
	perfil_logado = get_perfil_logado(request)
	perfil_logado.bloquear_perfil(perfil_id)
	return redirect('perfil')

@login_required
def desbloquear(request, bloqueio_id):
	bloqueio = Bloqueio.objects.get(id=bloqueio_id)
	bloqueio.desbloquear()
	return redirect('perfil')

@login_required
def excluir_post(request, post_id):
	post = Postagem.objects.get(id=post_id)
	post.excluir_post()
	return redirect('perfil')

class PostarView(View):

	template_name = 'postar.html'

	def get(self, request):
		form = PostarForm()
		return render(request, self.template_name, {'form':form, 'perfil_logado':get_perfil_logado(request)})

	def post(self, request):
		
		form = PostarForm(request.POST)
		
		if form.is_valid():
			dados_form = form.cleaned_data
			post = Postagem()
			post.texto = dados_form['texto']
			post.responsavel = get_perfil_logado(request)
			post.save()
			return redirect('perfil')


		return render(request, self.template_name, {'form':form, 'perfil_logado':get_perfil_logado(request)})
	
class BuscarView(View):

	def post(self, request):
		
		form = BuscarForm(request.POST)
		
		if form.is_valid():
			dados_form = form.cleaned_data
			resultado_busca = Perfil.objects.filter(nome__icontains= dados_form['username'])
			
			lista_nao_bloqueados = []	
			perfil_logado = get_perfil_logado(request)
			[lista_nao_bloqueados.append(resultado) for resultado in resultado_busca if resultado not in perfil_logado.perfis_que_me_bloquearam()]
					

			return render(request, 'busca.html', {'perfil_logado':get_perfil_logado(request), 'resultado_busca': lista_nao_bloqueados})


		return redirect('perfil')
	
