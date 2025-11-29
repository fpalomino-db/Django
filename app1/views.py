from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse
from .models import mascota

# Create your views here.

def home(request):
    return HttpResponse('Esta es mi primera ruta en django')

def saludo(request):
    return HttpResponse('Saludando desde la ruta /saludo')

def hola(request):
    mascotas = ['Luna','Dovi','Balto','Ayudante de santa']
    return render(request,'hola.html',{
        'nombre': 'Luis',
        'mascotas':mascotas
    })

def dashboard(request):
    if request.method == 'GET':
        mascotas = mascota.objects.all()
        filtro = request.GET.get("tipo","")
        if filtro:
            mascotas_filtradas = mascota.objects.filter(tipo=filtro)
        else:
            mascotas_filtradas = mascotas
        
        tipos = sorted({mascota.tipo for mascota in mascotas})

        return render(request,'dashboard.html',{
            "mascotas":mascotas_filtradas,
            "tipos":tipos,
            "filtro": filtro
        })
    elif request.method == 'POST':
        nombre_post = request.POST.get('nombre_post')
        edad_post = int(request.POST.get('edad_post'))
        tipo_post = request.POST.get('tipo_post')
        estado_post = request.POST.get('estado_post')

        mascota.objects.create(
            nombre=nombre_post,
            edad=edad_post,
            tipo=tipo_post,
            estado=estado_post
        )
        return HttpResponseRedirect(reverse('app1:dashboard'))
    else:
        print("Este metodo se revisara luego")
        return HttpResponseRedirect(reverse('app1:dashboard'))
    
def eliminarRegistro(request,idMascota):
    objMascota = mascota.objects.get(id=idMascota)
    objMascota.delete()
    return HttpResponseRedirect(reverse('app1:dashboard'))