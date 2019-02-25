from django.db import models

class Cofre(models.Model):

	def __str__(self):
		return self.nome_grupo

	adm = models.ForeignKey('Usuario', on_delete = models.CASCADE, related_name = 'Administrador')
	valor_total = models.DecimalField(max_digits = 10, decimal_places = 2)
	qtd_usuarios = models.IntegerField(blank = False, null = False)
	nome_grupo = models.CharField(max_length = 255, null = False)
	dt_meta = models.DateTimeField(blank = False, null = False)
	descricao = models.CharField(max_length = 255, null = False)
	transacoes = models.ManyToManyField('Usuario',through='Transacao', related_name='transacoes_recebidas')
	valor_atual = models.DecimalField(max_digits = 10, decimal_places = 2)

class Usuario(models.Model):


	def __str__(self):
		return self.nome

	saldo = models.DecimalField(max_digits = 10, decimal_places = 2)
	nome = models.CharField(max_length = 255, null = False)

	transacoes = models.ManyToManyField('Cofre',through='Transacao', related_name='transacoes_feitas')


	def depositar(self, valor_deposito, cofre_id):
		if self.saldo < valor_deposito:
			raise ValueError('Ops! Você não possui esse valor na carteira...')
		else:
			cofre = Cofre.objects.get(id=cofre_id)
			cofre.valor_atual += valor_deposito

			cofre.save()
			self.saldo -= valor_deposito


class Transacao(models.Model):
	Remetente = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = 'Remetente')
	Destinatario = models.ForeignKey(Cofre, on_delete = models.CASCADE, related_name = 'Destinatario')

	valor_transacao = models.DecimalField(max_digits = 10, decimal_places = 2)
	data_transacao = models.DateTimeField(blank = False, null = False)