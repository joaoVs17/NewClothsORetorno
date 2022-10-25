from traceback import print_tb
from django.db import models
from lojas.models import Loja
# Create your models here.

class ColecaoManager(models.Manager):
    def create_colecao(self, nome, loja):
        if not nome:
            raise ValueError ('É preciso dar um nome para a coleção')
        print(loja)
        colecao = self.model(loja = loja, nome = nome)
        colecao.save()
        return colecao
    def get_colecao(self, pk):
        if not pk:
            raise ValueError ('É preciso dar um nome para a coleção')
        colecao = self.objects.get(pk=pk)
        return colecao

class AbstractColecaoManager(models.Model):
    objects = ColecaoManager()
    class Meta:
        abstract = True

class Colecao(AbstractColecaoManager):
    loja = models.ForeignKey(Loja, on_delete= models.CASCADE, related_name='colecao')
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome