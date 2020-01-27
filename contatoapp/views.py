from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from contatoapp.forms import ContatoForm
from contatoapp.tasks import save_postview_taskscelery
from contatoapp.tasks import send_postview_taskscelery_com, send_postview_taskscelery_dir, send_postview_taskscelery_usu

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
 
            # pega o email que sera utilizado no email da valore e do usuario
            from_email = request.POST.get('email', '')

            # monta o email de aviso para a valore.io
            subject_1 = 'Formulario recebeu contato de cliente, assunto: ' + request.POST.get('subject', '')
            message_1 = from_email + ' , ' + request.POST.get('mensagem', '')

            # monta o email confirmacao para o usuario
            subject_2 = 'Contato com a Valore I/O'
            message_2 = 'Olá, obrigado por contatar a Valore I/O. Esta mensagem é para confirmar que nós recebermos o seu contato e que um de nossos profissionais irá entrar em contato rapidamente, usualmente dentro de 2 dias úteis. Obrigado, Valore I/O'

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

            #chama a funcao de tarefas assincronas do celery para gravar no database
            try:
                save_postview_taskscelery(request, reg)

            except Exception as e:
                messages.error(request, "The request wasn't sent to the queue because of error while loading the task queue-e1: {0}".format(e))
            else:
                try:
                    #coloca o email para o comercial na fila de tarefas assincronas
                    send_postview_taskscelery_com(request, reg, subject_1, message_1, from_email, subject_2, message_2)

                except Exception as e:
                    messages.error(request, "The request wasn't sent to the queue because of error while loading the task queue-e2: {0}".format(e))

                try:
                    #coloca o email para o diretor na fila de tarefas assincronas
                    send_postview_taskscelery_dir(request, reg, subject_1, message_1, from_email, subject_2, message_2)

                except Exception as e:
                    messages.error(request, "The request wasn't sent to the queue because of error while loading the task queue-e3: {0}".format(e))

                try:
                    #coloca o email para o usuario na fila de tarefas assincronas
                    send_postview_taskscelery_usu(request, reg, subject_1, message_1, from_email, subject_2, message_2)
                    messages.success(request, "The request and emails were sent to the queue. We will advice you accordingly! Please take a look at your spam email folder")
                except Exception as e:
                    messages.error(request, "The request wasn't sent to the queue because of error while loading the task queue-e4: {0}".format(e))

    form = ContatoForm() #clear form after submit

    return render(request, 'index.html', {'form' : form})
