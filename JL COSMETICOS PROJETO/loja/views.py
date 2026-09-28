from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProdutoForm, ClienteForm, PedidoForm
from .models import Produto, Cliente, Pedido

def home(request):
    return render(request,'loja/home.html', {'produtos': Produto.objects.filter(ativo=True)[:6], 'clientes': Cliente.objects.count(), 'pedidos': Pedido.objects.count()})

def produto_list(request):
    return render(request,'loja/produto_list.html', {'produtos': Produto.objects.all()})
def produto_create(request):
    form=ProdutoForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,'Produto cadastrado com sucesso!'); return redirect('produto_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Novo produto','voltar':'produto_list'})
def produto_update(request,pk):
    obj=get_object_or_404(Produto,pk=pk); form=ProdutoForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,'Produto atualizado!'); return redirect('produto_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Editar produto','voltar':'produto_list'})
def produto_delete(request,pk):
    obj=get_object_or_404(Produto,pk=pk)
    if request.method=='POST': obj.delete(); messages.success(request,'Produto excluído!'); return redirect('produto_list')
    return render(request,'loja/confirm_delete.html',{'obj':obj,'tipo':'produto','voltar':'produto_list'})

def cliente_list(request): return render(request,'loja/cliente_list.html',{'clientes':Cliente.objects.all()})
def cliente_create(request):
    form=ClienteForm(request.POST or None)
    if form.is_valid(): form.save(); messages.success(request,'Cliente cadastrado!'); return redirect('cliente_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Novo cliente','voltar':'cliente_list'})
def cliente_update(request,pk):
    obj=get_object_or_404(Cliente,pk=pk); form=ClienteForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,'Cliente atualizado!'); return redirect('cliente_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Editar cliente','voltar':'cliente_list'})
def cliente_delete(request,pk):
    obj=get_object_or_404(Cliente,pk=pk)
    if request.method=='POST': obj.delete(); messages.success(request,'Cliente excluído!'); return redirect('cliente_list')
    return render(request,'loja/confirm_delete.html',{'obj':obj,'tipo':'cliente','voltar':'cliente_list'})

def pedido_list(request): return render(request,'loja/pedido_list.html',{'pedidos':Pedido.objects.select_related('cliente','produto')})
def pedido_create(request):
    form=PedidoForm(request.POST or None)
    if form.is_valid():
        pedido=form.save(); messages.success(request,f'Pedido #{pedido.id} cadastrado!'); return redirect('pedido_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Novo pedido','voltar':'pedido_list'})
def pedido_update(request,pk):
    obj=get_object_or_404(Pedido,pk=pk); form=PedidoForm(request.POST or None,instance=obj)
    if form.is_valid(): form.save(); messages.success(request,'Pedido atualizado!'); return redirect('pedido_list')
    return render(request,'loja/form.html',{'form':form,'titulo':'Editar pedido','voltar':'pedido_list'})
def pedido_delete(request,pk):
    obj=get_object_or_404(Pedido,pk=pk)
    if request.method=='POST': obj.delete(); messages.success(request,'Pedido excluído!'); return redirect('pedido_list')
    return render(request,'loja/confirm_delete.html',{'obj':obj,'tipo':'pedido','voltar':'pedido_list'})
