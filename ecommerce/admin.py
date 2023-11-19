from django.contrib import admin
from ecommerce.models import Cliente, Pedido

class Clientes (admin.ModelAdmin):
    #abaixo são os mesmos dados encontrados em models.py da classe referida
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'endereco')
    list_display_links = ('id', 'nome') #campos escolhidos para alterar/editar na busca
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)


class Pedidos(admin.ModelAdmin):
    list_display = ('id', 'codigo_pedido', 'descricao', 'valor', 'loja')
    list_display_links = ('id', 'codigo_pedido')
    search_fields = ('codigo_pedido',)

admin.site.register(Pedido, Pedidos)