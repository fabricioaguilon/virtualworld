"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ListarAccesorios, ListarComputadoras, ListarImg, PagarView, BlankView, agregar_accesorio, agregar_computadora, eliminar_accesorio, eliminar_computadora, limpiar_accesorio, limpiar_computadora, restar_accesorio, restar_computadora

from . import views

urlpatterns = [
  #  path('index/', HomeView.as_view(), name='index'),
    path('index/', ListarImg.as_view(), name='index'),
    path('computadoras/', ListarComputadoras, name='computadoras'),
    path('accesorios/', ListarAccesorios, name='accesorios'),
    path('pagar/', PagarView.as_view(), name='pagar'),
    path('blank/', BlankView.as_view(), name='blank'),
    path('agregar/<int:producto_id>/', agregar_computadora, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_computadora, name="Del"),
    path('restar/<int:producto_id>/', restar_computadora, name="Sub"),
    path('limpiar/', limpiar_computadora, name="CLS"),
    path('aderir/<int:accesorio_id>/', agregar_accesorio, name="Agg"),
    path('eraser/<int:accesorio_id>/', eliminar_accesorio, name="Era"),
    path('rest/<int:accesorio_id>/', restar_accesorio, name="Rest"),
    path('Clean/', limpiar_accesorio, name="Clean"),

    # Registros
    path ('registro/', views.registro, name = "registro"),
    path ('login/', views.login_request, name = "login"),
    path ('logout/', views.logout_request, name = "logout"),



]
