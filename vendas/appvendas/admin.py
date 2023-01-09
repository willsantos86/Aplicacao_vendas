from django.contrib import admin
from appvendas.models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf']
    search_fields = ['nome', 'email', 'cpf']

class ItemInline(admin.StackedInline):
    model = Item
    extra = 1




class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data']
    inlines = [ItemInline]


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'produto', 'quantidade', 'preco']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Item, ItemAdmin)

