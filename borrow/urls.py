"""borrow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url
from django.urls import path
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
#    url(r'^login/$', auth_views.login),
    path('pessoa/', views.list_pessoas, name='url_list_pessoas'),
    path('pessoa/new/', views.new_pessoas, name='url_new_pessoas'),
    path('pessoa/<int:pk>/', views.edit_pessoas, name='url_edit_pessoas'),
    path('pessoa/<int:pk>/delete/', views.delete_pessoas, name='url_delete_pessoas'),

    path('endereco/', views.list_enderecos, name='url_list_enderecos'),
    path('endereco/new/', views.new_enderecos, name='url_new_enderecos'),
    path('endereco/<int:pk>/', views.edit_enderecos, name='url_edit_enderecos'),
    path('pessoa/<int:pk>/delete/', views.delete_enderecos, name='url_delete_enderecos'),

    path('item/', views.list_itens, name='url_list_itens'),
    path('item/new/', views.new_itens, name='url_new_itens'),
    path('item/<int:pk>/', views.edit_itens, name='url_edit_itens'),
    path('item/<int:pk>/delete/', views.delete_itens, name='url_delete_itens'),

    path('cessao/', views.list_cessoes, name='url_list_cessoes'),
    path('cessao/new/', views.new_cessoes, name='url_new_cessoes'),
    path('cessao/<int:pk>/', views.edit_cessoes, name='url_edit_cessoes'),
    path('cessao/<int:pk>/delete/', views.delete_cessoes, name='url_delete_cessoes'),

    url(r'^$', views.index, name='Index'),
    url(r'^admin/', admin.site.urls),

]

#from django.contrib import admin
#from django.urls import path
#from core import views
#from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#
#urlpatterns = [
#    path('admin/', admin.site.urls),
#    url('', auth_views.login, name='login'),
#    url(r'^login/$', auth_views.login, name='login'),
#    url(r'^logout/$', auth_views.logout, name='logout'),
#]

#from django.urls import path
##from usuarios.views import RegistrarUsuarioView
#from django.contrib.auth import views
#
#urlpatterns = [
#    #path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
#    path('login/', views.login, {'template_name': 'login.html'}, name='login'),
#    path('logout/', views.logout_then_login, {'login_url': '/login/'}, name='logout')
#]

#from django.contrib.auth import views as auth_views
#from django.conf.urls import url
#
#urlpatterns = [
#   url( r'^login/$',auth_views.LoginView.as_view(template_name="useraccounts/login.html"), name="login"),
#]