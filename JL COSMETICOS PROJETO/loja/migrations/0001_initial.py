from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name="Cliente",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("nome",models.CharField(max_length=120)),("email",models.EmailField(max_length=254,unique=True)),("telefone",models.CharField(blank=True,max_length=20)),("endereco",models.CharField(blank=True,max_length=200)),("criado_em",models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name="Produto",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("nome",models.CharField(max_length=120)),("categoria",models.CharField(max_length=80)),("descricao",models.TextField(blank=True)),("preco",models.DecimalField(decimal_places=2,max_digits=10)),("estoque",models.PositiveIntegerField(default=0)),("ativo",models.BooleanField(default=True))]),
        migrations.CreateModel(name="Pedido",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("quantidade",models.PositiveIntegerField(default=1)),("valor_unitario",models.DecimalField(decimal_places=2,max_digits=10)),("status",models.CharField(choices=[("PENDENTE","Pendente"),("PAGO","Pago"),("ENVIADO","Enviado"),("CONCLUIDO","Concluído"),("CANCELADO","Cancelado")],default="PENDENTE",max_length=20)),("criado_em",models.DateTimeField(auto_now_add=True)),("cliente",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="pedidos",to="loja.cliente")),("produto",models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name="pedidos",to="loja.produto"))])
    ]
