from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name = "perfil", on_delete = models.CASCADE)
    perfis_bloqueados = models.ManyToManyField('self')

    @property
    def super_user(self):
        return self.usuario.is_superuser

    @property
    def email(self):
        return self.usuario.email   

    def __str__(self):
        return self.nome

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self,convidado = perfil_convidado)
            convite.save()

    def pode_convidar(self, perfil_a_convidar):
        pode_convidar = False
        if perfil_a_convidar not in self.contatos.all():
            pode_convidar = True
        return pode_convidar

    def desfazer_amizade(self, perfil_id):
        self.contatos.remove(perfil_id)
    
    def setar_super_user(self):
        
        self.usuario.is_superuser = True 
        self.usuario.save()

    def bloquear_perfil(self, perfil_id):
        perfil = Perfil.objects.get(id=perfil_id)
        self.perfis_bloqueados.add(perfil)
    
    def desbloquear_perfil(self, perfil_id):
        perfil = Perfil.objects.get(id=perfil_id)
        self.perfis_bloqueados.remove(perfil)
    
    
    @property
    def perfis_nao_bloqueados(self):
        usuarios_nao_bloqueados = []
        for perfil in Perfil.objects.all():
            if perfil not in self.perfis_bloqueados.all():
                usuarios_nao_bloqueados.append(perfil)

        return usuarios_nao_bloqueados

    
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):        
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()
    
    def recusar(self):
        self.delete()    
        