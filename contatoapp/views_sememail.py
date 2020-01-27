from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from contatoapp.forms import ContatoForm

def index(request):
    context = RequestContext(request)
    form = ContatoForm()
    return render(request, 'index.html', {'form' : form}, context)

#http://thepythondjango.com/designing-custom-404-500-error-pages-django/
def error_404(request, exception):
    data = {}
    return render(request, 'ops404.html', data)

def error_500(request, exception):
    data = {}
    return render(request, 'ops500.html', data)

def error_502(request, exception):
    data = {}
    return render(request, 'ops502.html', data)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
 
            #chama a funcao de tarefas assincronas do celery
            #post_view_taskscelery.delay(request)

            # pega o email que sera utilizado no email da valore e do usuario
            from_email = request.POST.get('email', '')

            # monta o email de aviso para a valore.io
            subject_1 = 'Formulario recebeu contato de cliente, assunto: ' + request.POST.get('subject', '')
            message_1 = from_email + ' , ' + request.POST.get('mensagem', '')

            # monta o email confirmacao para o usuario
            subject_2 = 'Contato com a Valore I/O'
            message_2 = 'Olá, obrigado por contatar a Valore I/O. Esta mensagem é para confirmar que nós recebermos o seu contato e que um de nossos profissionais irá entrar em contato rapidamente, usualmente dentro de 2 dias úteis. Obrigado, Valore I/O'

            # envia o email para avisar o comercial da valore.io
#            try:
#                send_mail(subject_1, message_1, from_email, [settings.EMAIL_COMERCIAL])
#            except BadHeaderError:
#                return HttpResponse('Invalid header found.')

            # envia o email para avisar o diretor da valore.io
#            try:
#                send_mail(subject_1, message_1, from_email, [settings.EMAIL_DIRETOR])
#            except BadHeaderError:
#                return HttpResponse('Invalid header found.')

            # envia o email para tranquilizar o usuario
#            try:
#                send_mail(subject_2, message_2, settings.EMAIL_COMERCIAL, [from_email])
#            except BadHeaderError:
#                return HttpResponse('Invalid header found.') 

            # grava no Database
            reg = form.save(commit=True)
            try:
                x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
                if x_forwarded_for:
                    reg.ipaddress = x_forwarded_for.split(',')[0]
                else:
                    reg.ipaddress = request.META.get('REMOTE_ADDR')
            except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as e:
                erro = str(e)               #pega a mensagem de erro
                reg.ipaddress = erro[0:100] #pega os primeiros 100 caracteres da mensagem de erro
                reg.ipaddress = None

            try:
                reg.save()
                if reg.ipaddress:
                    messages.success(request, 'Success, it was inserted. Soon we will be back, thank you! Your IP is: ' + reg.ipaddress)
                else:
                    messages.success(request, 'Success, it was inserted. Soon we will be back, thank you!')
            except:
                messages.success(request, 'The message was NOT inserted. Sorry!')

    form = ContatoForm() #clear form after submit

    return render(request, 'index.html', {'form' : form})
