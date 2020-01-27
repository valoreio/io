from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin import site
from contatoapp.models import Contatos

class ContatosAdmin(admin.ModelAdmin):
    #campos que aparecem no form na ordem estabelecida 
    fields = ['name','email','phone','subject','mensagem','ipaddress','compayname','cnpjcpf','paymentmethod','agree_term_participation_privacy_SN']
    #campos que aparecem na query geral
    list_display = ['dt_criacao','name','email','phone','mensagem','status','ipaddress','dt_atualiz','compayname','cnpjcpf','subject','paymentmethod','agree_term_participation_privacy_SN']
    #campos que terao a opcao de ordenacao
    search_fields = ['dt_criacao','name','email','phone','mensagem','status','ipaddress','dt_atualiz','compayname','cnpjcpf','subject','paymentmethod','agree_term_participation_privacy_SN']
    #mostra o botao save no top
    save_on_top = True
    #campos que aparecem no form mas nao podem ser editados (just display)
    readonly_fields=['ipaddress']

site.register(Contatos, ContatosAdmin)
admin.site.site_title = 'Valore I/O'
admin.site.site_header = 'Messages & Contacts Valore I/O'
admin.site.index_title = 'Valore I/O, Messages & Contacts'
