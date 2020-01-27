from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
from django.db.models import EmailField
from django.db.models import TextField
from django.http import HttpRequest, request
from contatoapp.choices import *

class Contatos(models.Model):
    dt_criacao = models.DateTimeField(auto_now_add=True, verbose_name='initial date', db_column='dt_criacao')
    name = models.CharField(db_index=True, max_length=50, blank=True, null=True, verbose_name='name', db_column='name')
    email = models.EmailField(max_length=70, blank=True, null=True, verbose_name='e-mail', db_column='email')
    mensagem = models.TextField(max_length=300, blank=True, null=True, verbose_name='description', db_column='mensagem')
    status = models.BooleanField(default=False, verbose_name='status', db_column='status')
    ipaddress = models.CharField(max_length=100, blank=True, null=True, verbose_name='your IP Address', db_column='ipaddress')
    dt_atualiz = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='updated date', db_column='dt_atualiz')
    phone = models.CharField(max_length=25, blank=True, null=True, verbose_name='phone', db_column='phone')
    compayname = models.CharField(db_index=True, max_length=50, blank=True, null=True, verbose_name='companyname', db_column='companyname')
    cnpjcpf = models.CharField(db_index=True, max_length=25, blank=True, null=True, verbose_name='cnpjcpf', db_column='cnpjcpf')
    subject = models.CharField(db_index=True, max_length=20, blank=True, null=True, choices=SUBJECT_CHOICES, default=6, verbose_name='subject', db_column='subject')
    paymentmethod = models.CharField(db_index=True, max_length=20, blank=True, null=True, choices=PAYMENTMETHODS_CHOICES, verbose_name='paymentmethod', db_column='paymentmethod')
    agree_term_participation_privacy_SN = models.CharField(db_index=True, max_length=1, blank=True, null=True, choices=AGREE_CHOICES, default=1, verbose_name='agree_term_participation_privacy_SN', db_column='agree_term_participation_privacy_SN')

    def __str__(self):   # __unicode__ on Python 2
        return self.name

    class Meta:
        verbose_name_plural="Contatos"
        ordering = ["-dt_criacao", "mensagem"]
