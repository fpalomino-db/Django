from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse


# Create your views here.
def hola(request):
    return HttpResponse('Hola')