from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
	perfil_logado = get_perfil_logado(request)
	usuarios_nao_bloqueados = perfil_logado.perfis_nao_bloqueados
	return render(request, 'index.html',{'perfis' : usuarios_nao_bloqueados, 'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir_perfil(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)

	return render(request, 'perfil.html',
		          {'perfil' : perfil, 
				   'perfil_logado' : get_perfil_logado(request)})



@login_required
def convidar(request,perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id) 
	perfil_logado = get_perfil_logado(request) 
	
	if(perfil_logado.pode_convidar(perfil_a_convidar)):
		perfil_logado.convidar(perfil_a_convidar)
	
	return  redirect('index')

@login_required
def get_perfil_logado(request):

	return request.user.perfil

@login_required
def aceitar(request, convite_id):
	
	convite = Convite.objects.get(id = convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def recusar(request, convite_id):
	
	convite = Convite.objects.get(id = convite_id)
	convite.recusar()
	return redirect('index')

@login_required
def desfazer_amizade(request, perfil_id):

	perfil_logado = get_perfil_logado(request)
	perfil_logado.desfazer_amizade(perfil_id)
	return redirect('index')

@login_required
def setar_super_user(self, perfil_id):
	
	perfil = Perfil.objects.get(id = perfil_id)
	perfil.setar_super_user()
	return redirect('index')

@login_required
def bloquear_perfil(request, perfil_id):
	perfil_logado = get_perfil_logado(request)
	perfil_logado.bloquear_perfil(perfil_id)
	return redirect('index')

@login_required
def desbloquear_perfil(request, perfil_id):
	perfil_logado = get_perfil_logado(request)
	perfil_logado.desbloquear_perfil(perfil_id)
	return redirect('index')
