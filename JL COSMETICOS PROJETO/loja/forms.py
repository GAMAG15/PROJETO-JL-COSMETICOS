from django import forms
from .models import Produto, Cliente, Pedido

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','categoria','descricao','preco','estoque','ativo']
        widgets = {'descricao': forms.Textarea(attrs={'rows':3}), 'preco': forms.NumberInput(attrs={'step':'0.01','min':'0'})}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','email','telefone','endereco']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente','produto','quantidade','valor_unitario','status']
        widgets = {'quantidade': forms.NumberInput(attrs={'min':'1'}), 'valor_unitario': forms.NumberInput(attrs={'step':'0.01','min':'0'})}
