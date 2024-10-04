from django.shortcuts import render
# Create your views here.



def index(request):
    return render(request,"index.html")

def clientes(request):
    return render(request,"clientes.html")

def cuenta(request):
    return render(request,"cuenta.html")

def empleados(request):
    return render(request,"empleado.html")

def productos(request):
    return render(request,"productos.html")





