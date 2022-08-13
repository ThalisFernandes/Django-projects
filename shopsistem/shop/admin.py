from django.contrib import admin
from shop.models import *

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_prod', 'descricao','price', 'estabelecimento_id')

class estabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'contato', 'status')

admin.site.register(produto, ProdutoAdmin)
admin.site.register(estabelecimento, estabelecimentoAdmin)

