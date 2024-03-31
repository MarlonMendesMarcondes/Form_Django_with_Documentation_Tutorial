from django.shortcuts import redirect, render
from .models import Formulario
# Create your views here.


def formulario(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        
        return render(request, 'formulario.html',{'status':status})
    elif request.method == 'POST':
        nomedigitado = request.POST.get('nome')
        idadedigitado = request.POST.get('idade')
        formulario = Formulario(
            nome = nomedigitado,
            idade = idadedigitado
            
        )
        formulario.save()
        
        return redirect('/formulario/?status=1')
    
        
#        nome = request.POST.get('nome')
#        idade = request.POST.get('idade')
#        return HttpResponse(f'{nome} e tem {idade} anos de idade')