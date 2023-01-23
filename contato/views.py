from django.shortcuts import render
from contato.models import Contato
from contato.forms import ContatoForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def quem_somos(request):
    return render(request, 'quem-somos.html')


def contato(request):
    data = {
        'form': ContatoForm()
    }

    if request.method == 'POST':
        formulario = ContatoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensagem'] = 'contato.salvo'
        else:
            data['form'] = formulario


    return render(request, 'contato.html', data)