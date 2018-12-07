# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User, UserManager


# Create your models here.

# Classe para registrar o endereço das pessoas ou onde itens podem ser pego para emprestimo
class Endereco(models.Model):
    rua = models.CharField(max_length=200, name='Rua')
    numero = models.CharField(max_length=10, name='Numero')
    complemento = models.CharField(max_length=200, name='Complemento')
    cidade = models.CharField(max_length=200, name='Cidade')
    estado = models.CharField(max_length=2, name='Estado')
    cep = models.CharField(max_length=10, name='CEP')

    class Meta:
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.Rua + ' , ' + str(self.Numero)

    # Classe para registrar pessoas que podem emprestar ou pedir emprestado


# herda da classe User para usar com autenticação
class Pessoa(models.Model):
    # user = models.OneToOneField(User, related_name='profile',on_delete=models.CASCADE)
    #nome = models.CharField(max_length=200, name='Nome')
    nome = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.nome



# Classe para registrar como está o emprestimo
# solicitado, emprestado, esperando retirada, devolvido, esperando aprovação de devolução
class Status(models.Model):
    Descricao = models.CharField(
        max_length=100,
        choices = (
        ('1','Solicitado'),
        ('2','Emprestado'),
        ('3','Devolvido'),
        ('4','Esperando retirada'),
        ('5','Esperando aprovação da devolução'),
        )
    )

    class Meta:
        verbose_name_plural = 'Status'


# Classe para criação de Itens que podem ser emprestados
class Item(models.Model):
    nome = models.CharField(max_length=200, name='Nome')
    descricao = models.TextField(name='Descrição')
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome

    class Meta:
        verbose_name_plural = 'Itens'


# Classe para informar quando um produto está disponível
class Cessao(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    data_hora_inicio = models.DateTimeField(blank=False, null=False)
    data_hora_final = models.DateTimeField(blank=False, null=False)
    local = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    raio = models.IntegerField
    valor_item = models.DecimalField(max_digits=7, decimal_places=2)
    valor_emprestimo = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Cessões'

    def __str__(self):
        return self.item.Nome


# Classe para registrar os empréstimos
class Emprestimo(models.Model):
    data_hora_emprestimo = models.DateTimeField(name='Data e Hora de empréstimo')
    data_hora_devolucao = models.DateTimeField(name='Data e Hora de devolução')
    data_hora_previsao_devolucao = models.DateTimeField('Previsão de entrega')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cessao = models.ForeignKey(Cessao, on_delete=models.CASCADE)
    cedido = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Empréstimos'
