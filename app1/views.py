from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse


# Create your views here.

def home(request):
    return HttpResponse('Esta es mi primera ruta en django')
def saludo(request):
    return HttpResponse('Hola mundo')
def hola(request):
    mascotas = ['Luna', 'Dovi','Hosh','Tú','Tumama', 'Hachi']
    return render(request, 'hola.html',{
        'nombre': 'Fabrizio',
        'mascotas': mascotas
    })
