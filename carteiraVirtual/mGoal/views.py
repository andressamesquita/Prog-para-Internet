from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index (request):
	return render(request, 'index.html')


def exibir_usuario(request, usuario_id):
	usuario = Usuario.objects.get(id=usuario_id)
	return render(request, 'usuario.html', { "usuario":usuario })


def exibir(request):
	return render(request, 'listaUser.html', {"mGoal":Usuario.objects.order_by('nome')})

def transferencia(request, usuario_id):
    if request.method =='POST':
        form = TransferenciaForm(request.POST)

        if form.is_valid():
            transferencia = form.save(commit=False)
            remetente = Usuario.objects.get(id=usuario_id)
            transferencia.Remetente = remetente
            transferencia.Destinatario = form.cleaned_data['Destinatario']
            transferencia.valor_transacao = form.cleaned_data['valor_transacao']
            transferencia.data_transacao = form.cleaned_data['data_transacao']
            u = Usuario.objects.get(id=transferencia.Remetente.id)
            c = transferencia.Destinatario.id
            u.depositar(transferencia.valor_transacao,c)
            u.save()
            transferencia.save()
            return redirect('exibir_usuario', transferencia.Remetente.id)
    else:
        form = TransferenciaForm()
        return render(request, 'transferencia.html', {'form': form})



def exibir_cofre(request, cofre_id):
    cofre = Cofre.objects.get(id=cofre_id)
    
    lista_transacao = []
    for  transacao in cofre.transacoes_feitas.all():
        if transacao not in lista_transacao:
            lista_transacao.append(transacao)

    return render(request, 'cofre.html', {"cofre":cofre,'transacoes':lista_transacao})


def form_cofre(request, usuario_id):

    if request.method =='POST':
        form = CofreForm(request.POST)

        if form.is_valid():
            cofre = form.save(commit=False)
            usuario = Usuario.objects.get(id=usuario_id)
            cofre.adm = usuario
            cofre.valor_total = form.cleaned_data['valor_total']
            cofre.qtd_usuarios = form.cleaned_data['qtd_usuarios']
            cofre.nome_grupo = form.cleaned_data['nome_grupo'].title()
            cofre.dt_meta = form.cleaned_data['dt_meta']
            cofre.descricao = form.cleaned_data['descricao'].lower()
            cofre.valor_atual = 0
            cofre.save()
            return redirect('exibir_usuario', cofre.adm.id)
    else:
        form = CofreForm()
        return render(request, 'formCofre.html', {'form': form})


def cadastro_usuario(request):

    if request.method =='POST':
        form = UserForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nome = form.cleaned_data['nome']
            usuario.saldo = form.cleaned_data['saldo']
            
            usuario.save()
            return redirect('exibir_usuario', usuario.id)
    else:
        form = UserForm()
        return render(request, 'formCadUser.html', {'form': form})
