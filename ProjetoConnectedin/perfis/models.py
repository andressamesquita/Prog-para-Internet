from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name = "perfil", on_delete = models.CASCADE)
    contatos_bloqueados = models.ManyToManyField('self', related_name = 'meus_contatos_bloqueados', symmetrical=False, through= 'Bloqueio')
   # img_perfil = models.ImageField(upload_to = "static/img/perfil/",blank=True)

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
    
    def mostrar_perfil(self, perfil_a_exibir):

        pode_mostrar = True
        for perfil in perfil_a_exibir.bloqueios_feitos.all():
            if perfil.perfil_bloqueado.id == self.id:
                return False
            
        return pode_mostrar

    def pode_convidar(self, perfil_a_convidar):

        pode_convidar = False
        convites = Convite.objects.filter(solicitante=self, convidado=perfil_a_convidar).all()
        
        if len(convites) == 0 and perfil_a_convidar not in self.contatos.all():
            pode_convidar = True
        return pode_convidar

    def desfazer_amizade(self, perfil_id):
        self.contatos.remove(perfil_id)
    
    def setar_super_user(self):
        
        self.usuario.is_superuser = True 
        self.usuario.save()

    def pode_bloquear(self, perfil_a_bloquear):

        pode_bloquear = True
        
        for perfil in self.bloqueios_feitos.all():
            if perfil.perfil_bloqueado.id == perfil_a_bloquear.id:
                return False
            
        return pode_bloquear

    def bloquear_perfil(self, perfil_id):
        perfil = Perfil.objects.get(id=perfil_id)
        bloqueio = Bloqueio()
        bloqueio.perfil_que_bloqueia = self
        bloqueio.perfil_bloqueado = perfil
        bloqueio.save()
    
    @property
    def bloqueios_feitos(self): #meus_bloqueios
        return Bloqueio.objects.filter(perfil_que_bloqueia=self)

    
    def perfis_que_me_bloquearam(self):

        perfis_bloquearam, perfis = Bloqueio.objects.filter(perfil_bloqueado=self), []
        [perfis.append(bloqueio.perfil_que_bloqueia) for bloqueio in perfis_bloquearam]
        return perfis
    
    @property
    def minhas_postagens(self):
        postagem = Postagem.objects.filter(id = self.id)
        return postagem

class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):        
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()
    
    def recusar(self):
        self.delete()


class Postagem(models.Model):

    texto = models.CharField(max_length=255, null=False)
    dt_publicacao = models.DateTimeField(default=timezone.now)
    responsavel = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='minhas_postagens' )
   

    def __str__(self):
        return self.texto

    def excluir_post(self):
        self.delete()

    class Meta:
        ordering = ['-dt_publicacao']



class Bloqueio(models.Model):

    perfil_que_bloqueia = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='perfis_que_bloqueei')
    perfil_bloqueado = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='perfis_que_estou_bloqueado')

    def desbloquear(self):
        self.delete()
