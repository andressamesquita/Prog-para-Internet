from django.db import models
import random

class Url(models.Model):
    
    texto_url = models.CharField(max_length=255)
    url_encurtada = models.CharField(max_length=50)


    def encurta_url(self):
        #gera um numero aleatorio
        #concatena com uma string
        #atualiza o field url_encurtada

        numb_aleatorio = random.randint(1,100)
        hash = 'tVa'+ str(numb_aleatorio)
        self.url_encurtada = 'http://localhost:8000/'+ hash
        return self.url_encurtada
