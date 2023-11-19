from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=40)

    def __str__(self):
        return self.nome
    

class Pedido(models.Model):
    codigo_pedido = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    valor = models.CharField(max_length=10)
    loja = models.CharField(max_length=20)
 