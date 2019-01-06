from django.db import models
from perfis.models import *

# Create your models here.
class Timeline(models.Model):
    
    perfil = models.OneToOneField(Perfil, related_name = "minha_timeline", on_delete = models.CASCADE)

    def get_timeline(self):
        lista_postagens = []
        postagens_ordenadas = Postagem.objects.all().order_by('dt_publicacao')[::-1]

        for i in postagens_ordenadas:
            if i.responsavel in self.perfil.contatos.all() or i.responsavel.id == self.perfil.id:
                lista_postagens.append(i)
        
        return lista_postagens
