from django.urls import path
from AppProyecto.views import *
from . import views
from .views import UsuarioEdicion
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", views.home, name="home"),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('logout/', LogoutView.as_view(template_name='AppProyecto/logout.html'), name='logout'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),
    path('ventaCreacion/', VentaCreacion.as_view(), name='nuevo'),
    #URLS DEL AUTO
    path('autoDetalle/<int:pk>/', AutoDetalle.as_view(), name='auto'),
    path('listaAuto/', AutoLista.as_view(), name='autos'),
    path('autoBorrado/<int:pk>/', AutoDelete.as_view(), name='auto_eliminar'),
    path('autoEdicion/<int:pk>/', AutoUpdate.as_view(), name='auto_editar'),
    path('autoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    #URLS DE LAS BICICLETAS
    path('bicicletaDetalle/<int:pk>/', BicicletaDetalle.as_view(), name='bicicleta'),
    path('listaBicicleta/', BicicletaLista.as_view(), name='bicicletas'),
    path('bicicletaBorrado/<int:pk>/', BicicletaDelete.as_view(), name='bicicleta_eliminar'),
    path('bicicletaEdicion/<int:pk>/', BicicletaUpdate.as_view(), name='bicicleta_editar'),
    path('bicicletaDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
#URL PARA LAS MOTOS
    path('motoDetalle/<int:pk>/', MotoDetalle.as_view(), name='moto'),
    path('listaMoto/', MotoLista.as_view(), name='motos'),
    path('motoBorrado/<int:pk>/', MotoDelete.as_view(), name='moto_eliminar'),
    path('motoEdicion/<int:pk>/', MotoUpdate.as_view(), name='moto_editar'),
    path('motoDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
#URL PARA LOS MONOPANINES
    path('monopatinesDetalle/<int:pk>/', MonopatinDetalle.as_view(), name='monopatin'),
    path('listaMonopatin/', MonopatinLista.as_view(), name='monopatines'),
    path('monopatinBorrado/<int:pk>/', MonopatinDelete.as_view(), name='monopatin_eliminar'),
    path('monopatinEdicion/<int:pk>/', MonopatinUpdate.as_view(), name='monopatin_editar'),
    path('monopatinDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
#URL PARA VARIOS
    path('variosDetalle/<int:pk>/', VariosDelete.as_view(), name='vario'),
    path('listaVarios/', VariosLista.as_view(), name='varios'),
    path('variosBorrado/<int:pk>/', VariosDelete.as_view(), name='vario_eliminar'),
    path('variosEdicion/<int:pk>/', VariosUpdate.as_view(), name='vario_editar'),
    path('varioDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='vario'),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),


]