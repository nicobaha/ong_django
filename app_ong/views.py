from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    mensaje = "¡Bienvenido a la página de inicio de nuestra ONG!"
    return render(request, 'app_ong/index.html', {'mensaje': mensaje})

def proyectos(request):
    return render(request, 'app_ong/proyectos.html')  # Sin contexto adicional