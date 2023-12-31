"""
URL configuration for todoProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from todoApp import views
from todoApp.models import Evento

urlpatterns = [
    path('', views.redirectView),
    path('index/', views.indexView),
    path('index/<int:evento_id>/', views.eventoById),
    path('index/<int:evento_id>/delete/', views.delete_evento),
    path('login/', views.loginView),
    path('novoEventoForm/', views.novoEventoForm),
]
