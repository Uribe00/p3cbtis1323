from django.urls import path
from . import views
urlpatterns =[
    path("",views.index, name="index"),
    path("clientes/",views.clientes, name="clientes"),
    path("cuenta/",views.cuenta, name="cuenta"),
    path("empleados/",views.empleados, name="empleado"),
    path("productos/",views.productos, name="producto")
]

