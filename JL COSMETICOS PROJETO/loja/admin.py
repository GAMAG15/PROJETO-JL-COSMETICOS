from django.contrib import admin
from .models import Produto, Cliente, Pedido
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin): list_display=('nome','categoria','preco','estoque','ativo'); search_fields=('nome','categoria')
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin): list_display=('nome','email','telefone','criado_em'); search_fields=('nome','email')
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin): list_display=('id','cliente','produto','quantidade','valor_unitario','status','criado_em'); list_filter=('status',)
