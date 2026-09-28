from django.urls import path
from . import views
urlpatterns = [
 path('',views.home,name='home'),
 path('produtos/',views.produto_list,name='produto_list'), path('produtos/novo/',views.produto_create,name='produto_create'), path('produtos/<int:pk>/editar/',views.produto_update,name='produto_update'), path('produtos/<int:pk>/excluir/',views.produto_delete,name='produto_delete'),
 path('clientes/',views.cliente_list,name='cliente_list'), path('clientes/novo/',views.cliente_create,name='cliente_create'), path('clientes/<int:pk>/editar/',views.cliente_update,name='cliente_update'), path('clientes/<int:pk>/excluir/',views.cliente_delete,name='cliente_delete'),
 path('pedidos/',views.pedido_list,name='pedido_list'), path('pedidos/novo/',views.pedido_create,name='pedido_create'), path('pedidos/<int:pk>/editar/',views.pedido_update,name='pedido_update'), path('pedidos/<int:pk>/excluir/',views.pedido_delete,name='pedido_delete'),
]
