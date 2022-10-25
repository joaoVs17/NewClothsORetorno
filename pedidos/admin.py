from django.contrib import admin
from .models import StatusPedido, Pedido, PedidoConcluido, Item

# Register your models here.
admin.site.register(Pedido)
admin.site.register(StatusPedido)
admin.site.register(PedidoConcluido)
admin.site.register(Item)
