from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    categoria = models.CharField(max_length=80)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS = [('PENDENTE','Pendente'),('PAGO','Pago'),('ENVIADO','Enviado'),('CONCLUIDO','Concluído'),('CANCELADO','Cancelado')]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='pedidos')
    quantidade = models.PositiveIntegerField(default=1)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDENTE')
    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.quantidade * self.valor_unitario

    def __str__(self):
        return f'Pedido #{self.pk} - {self.cliente.nome}'
