from django.contrib import admin
from .models import Categoria,Roupa, Tamanho

# Register your models here.
admin.site.register(Roupa)
admin.site.register(Tamanho)
admin.site.register(Categoria)