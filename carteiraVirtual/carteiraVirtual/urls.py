"""carteiraVirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mGoal.views import *
from django.conf.urls import include, url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('usuario/<int:usuario_id>', exibir_usuario, name = 'exibir_usuario'),
    path('lista/', exibir, name = 'exibir_lista'),
    path('cofre/<int:cofre_id>', exibir_cofre, name = 'exibir_cofre'),
    path('transferencia/<int:usuario_id>', transferencia, name = 'transferencia'),
    path('form_cofre/<int:usuario_id>', form_cofre, name='cofre'),
    path('cadastro_usuario/', cadastro_usuario, name = 'new_usuario'),
    
    url('', include('pwa.urls')), # You MUST use an empty string as the URL prefix

]
