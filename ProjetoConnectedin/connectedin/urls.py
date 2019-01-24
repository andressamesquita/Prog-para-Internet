"""connectedin URL Configuration

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
from django.urls import path, include
from django.urls import path
from perfis import views 
from usuarios.views import *
from django.contrib.auth import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>/convidar',views.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar',views.aceitar, name='aceitar'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/', v.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', v.LogoutView.as_view(template_name = 'login.html'), name = 'logout'),
    path('convite/<int:convite_id>/recusar', views.recusar, name='recusar'),
    path('perfil/<int:perfil_id>/desfazer', views.desfazer_amizade, name='desfazer'),
    path('perfil/<int:perfil_id>/super', views.setar_super_user , name='super'),
    path('alterar_senha', mudarSenhaView.as_view(), name='mudar_senha'),
    path('perfil/<int:perfil_id>/bloquear', views.bloquear_perfil, name='bloquear'),
    path('perfil/<int:bloqueio_id>/desbloquear', views.desbloquear, name='desbloquear'),
    path('perfil/postar', views.PostarView.as_view(), name='postar'),
    path('perfil/<int:post_id>/excluir', views.excluir_post, name='excluir_post'),
    path('perfil/buscar', views.BuscarView.as_view(), name='buscar'),
    path('perfis/', include('django.contrib.auth.urls')),
   
]
'''
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    '''
    