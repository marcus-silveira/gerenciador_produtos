from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from plataforma.forms import ContatoForm


def index(request):
    return render(request, 'plataforma/index.html')


def contato(request):
    form = ContatoForm(
        request.POST or None
    )

    if str(request.method) == 'POST':
        print(f'meta {request.META}')
        if form.is_valid():
            form.clean()
            form = ContatoForm()

            messages.success(request, 'E-mail enviado com sucesso')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Erro ao tentar enviar E-mail')

    context = {
        'form': form
    }
    return render(request, 'plataforma/contato.html', context)


def produto(request):
    return render(request, 'plataforma/produto.html')
