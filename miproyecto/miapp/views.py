from django.shortcuts import render
from django.http import HttpResponse    



# Create your views here.

def saludo(request):
    return HttpResponse("¡Hola, bienvenido a Kamartasch, Que tal!") # Cuando la pagina solicite una respuesta, devolvera este mensaje

def info(request):
    return render(request,"datos.html")  # Renderiza la plantilla datos.html