from random import choices
from signal import raise_signal
from django.db import models
from django.utils import timezone
from hashlib import sha256
import re
from django.core.files.storage import FileSystemStorage
import os
#LOCAL
from users.models import User
from enderecos.models import Endereco

# Create your models here.
class Plano(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField()

    def __str__(self):
        return self.nome

class LojaManager(models.Manager):
    def pesquisa_lojas(self, query):
        if query:
            resultado = self.model.objects.filter(nome_loja__icontains=query).order_by('nome_loja')
        else:
            resultado = self.model.objects.all().order_by('nome_loja')
        return resultado
    def custom_encode_Sha(self, valor):
        valor = sha256(valor.encode()).hexdigest()
        return valor
    def valida_cnpj(self, cnpj):
        formato_cnpj = '^\d{2}.\d{3}.\d{3}/\d{4}-\d{2}'
        is_valido = re.match(formato_cnpj, cnpj)
        return bool(is_valido)
    def normalize_email(cls, email):
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    def create_loja(self, loja_admin, nome_loja,cnpj, numero_cartao, nome_cartao, cvv, plano, **other):
        if not cnpj:
            raise ValueError('Toda loja deve possuir um cnpj')
        if self.valida_cnpj(cnpj) is not True:
            raise ValueError('Todo CNPJ deve ser da forma xx.xxx.xxx./xxxx-xx')
        if not numero_cartao:
            raise ValueError('Toda loja deve possuir um número de cartão')
        if not nome_cartao:
            raise ValueError('É necessário saber o nome do cartão')
        if not cvv:
            raise ValueError('É necessário possuir o código de segurança do cartão')
        if not nome_loja:
            raise ValueError('Toda loja deve possuir um nome') 
        if not plano:
            raise ValueError('Toda loja deve possuir um plano')
        plano = Plano.objects.get(nome = plano.capitalize())
        numero_cartao = self.custom_encode_Sha(numero_cartao)
        nome_cartao = self.custom_encode_Sha(nome_cartao)
        cvv = self.custom_encode_Sha(cvv)

        loja = self.model(loja_admin=loja_admin,nome_loja=nome_loja, numero_cartao=numero_cartao, nome_cartao=nome_cartao, cvv=cvv, plano=plano, **other)
        loja.save()
        loja_admin.set_grupo('usuario_dono_loja')
        return loja

class AbstractLojaManager(models.Model):
    objects = LojaManager()
    class Meta:
        abstract=True

class Loja(AbstractLojaManager):

    loja_admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='loja')

    nome_loja = models.CharField(max_length=50)
    email_loja = models.EmailField(max_length=255, null=True)
    telefone_loja = models.CharField(max_length=16, null=True)
    cnpj = models.CharField(max_length=18)
    endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE, related_name='loja')

    numero_cartao = models.CharField(max_length=64)
    nome_cartao = models.CharField(max_length=64)
    cvv = models.CharField(max_length=64)
    data_expiracao = models.DateTimeField(64)

    date_joined_loja = models.DateTimeField(default=timezone.now)

    logo_loja = models.ImageField(upload_to='logos_lojas/',null=True)

    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)

    def alter_fields(self, fields, values):
        if len(fields) != len(values):
            raise ValueError('As listas de campos e valores devem ter tamanhos iguais')
        for field, value in zip(fields, values):
            if value and not value.isspace():
                setattr(self, field, value)
            self.save()
    def set_logo_loja(self,caminho, uploadImage, request):
        if request.FILES:
            fs = FileSystemStorage(location='media/'+caminho+'/', base_url='/'+caminho+'/')
            upload = request.FILES[uploadImage]
            upload_name = upload.name
            upload_name = upload_name.replace(" ", "")
            upload_name = upload_name.replace("ç","c")
            filename = fs.save(upload.name.replace(" ",""), upload)
            url = fs.url(filename)
            if url:
                if self.logo_loja:
                    currentDirectory=os.getcwd()
                    fs.delete(currentDirectory+self.logo_loja.url)
                setattr(self, 'logo_loja', url)
                self.save()


    def __str__(self):
        return self.nome_loja