from django.db import models
import re

# Creat your models here.
class EnderecoManager(models.Manager):
    def valida_cep(self, cep):
        padrao = '^\d{5}-\d{3}$'
        is_valido = re.match(padrao, cep)
        return bool(is_valido)
    def create_endereco(self, cep, estado, cidade, bairro, rua, numero, **other):
        if self.valida_cep(cep) is not True:
            raise ValueError('Todo CEP deve seguir a forma xxxxx-xxx')
        endereco = self.model(cep=cep, estado=estado, cidade=cidade, bairro=bairro, rua=rua, numero=numero, **other)
        endereco.save()
        return endereco
    def easy_create_endereco(self, fields, values):
        if len(fields) != len(values):
            raise ValueError('Ambas as listas devem ter o mesmo tamanho')
        endereco = self.model()
        endereco.save()
        for field, value in zip(fields, values):
            if value and not value.isspace():
                setattr(endereco, field, value)
            else:
                raise ValueError('Não deixe de inserir nenhum dado')
        endereco.save()
        return endereco 
    
    """ def alter_endereco(self, cep, estado, cidade, bairro, rua, numero, user):
        if self.valida_cep(cep) is not True:
            raise ValueError('Todo CEP deve seguir a forma xxxxx-xxx')
        pass """

class AbstractEnderecoManager(models.Model):
    objects = EnderecoManager()
    class Meta:
        abstract=True

class Endereco(AbstractEnderecoManager):

    cep = models.CharField(max_length=9)
    estado = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, null=True, blank=True)

    def valida_cep(self, cep):
        padrao = '^\d{5}-\d{3}$'
        is_valido = re.match(padrao, cep)
        return bool(is_valido)
    def set_cep(self, cep):
        if not self.valida_cep(cep):
            raise ValueError('Todo CEP deve seguir a forma xxxxx-xxx')
        self.cep = cep
        self.save()
    def set_estado(self, estado):
        self.estado = estado
        self.save()
    def set_cidade(self, cidade):
        self.cidade = cidade
        self.save()
    def set_bairro(self, bairro):
        self.bairro = bairro
        self.save()
    def set_rua(self, rua):
        self.rua = rua
        self.save()
    def set_numero(self, numero):
        self.numero = numero
        self.save()
    


