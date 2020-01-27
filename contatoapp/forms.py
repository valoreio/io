from django import forms
from django.forms import ModelForm
from contatoapp.models import Contatos
from contatoapp.choices import *
    
#http://stackoverflow.com/questions/5949723/custom-label-in-django-formset
class ContatoForm(forms.ModelForm):

    name = forms.CharField(label="Name*", max_length=50, required=True, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    email = forms.EmailField(label="e-mail*", max_length=70, required=True, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    phone = forms.CharField(label='Phone', max_length=25, required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    subject = forms.CharField(label='Subject*', max_length=20, required=True, widget=forms.Select(choices=SUBJECT_CHOICES))
    mensagem = forms.CharField(label="Message*", max_length=300, required=True, widget=forms.Textarea(attrs={'cols': 30, 'rows': 3, 'onKeyUp': 'JSmensagemcounter()'}))
    companyname = forms.CharField(label="Company Name", max_length=50, required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    cnpjcpf = forms.CharField(label='CNPJ/CPF', max_length=25, required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 1}))
    paymentmethod = forms.CharField(label='Payment Method', max_length=20, required=False, widget=forms.Select(choices=PAYMENTMETHODS_CHOICES))
    agree_term_participation_privacy_SN = forms.CharField(label='Do you agree with the Term of Participation and Privacy?', max_length=1, required=False, widget=forms.Select(choices=AGREE_CHOICES))

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Contatos
        fields = ["name", "email", "phone", "subject", "mensagem", "companyname", "cnpjcpf", "paymentmethod", "agree_term_participation_privacy_SN"]
