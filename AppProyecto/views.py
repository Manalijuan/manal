from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,UpdateView,DetailView,ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import FormularioRegistroUsuario, FormularioEdicion,FormularioCambioPassword
from django.views.generic.edit import FormView,UpdateView
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from .models import Vendedor, Comentario
from .forms import FormularioNuevaVenta,ActualizacionAuto, FormularioComentario, ActualizacionBicicleta,ActualizacionMoto,ActualizacionMonopatines,ActualizacionVarios
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'AppProyecto/home.html')
class LoginPagina(LoginView):
    template_name = 'AppProyecto/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
class RegistroPagina(FormView):
    template_name = 'AppProyecto/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)
class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'AppProyecto/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'AppProyecto/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')
def password_exitoso(request):
    return render(request, 'AppProyecto/passwordExitoso.html', {})

class VentaCreacion(LoginRequiredMixin, CreateView):
    model = Vendedor
    form_class = FormularioNuevaVenta
    success_url = reverse_lazy('home')
    template_name = 'AppProyecto/ventaCreacion.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VentaCreacion, self).form_valid(form)  
     
     # CONFIGURACIONES DEL AUTO
class AutoDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'auto'
    template_name = 'AppProyecto/autoDetalle.html'

class AutoLista(LoginRequiredMixin, ListView):
    context_object_name = 'autos'
    queryset = Vendedor.objects.filter(articulo__startswith='auto')
    template_name = 'AppProyecto/listaAuto.html'
    login_url = '/login/'
class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('autos')
    context_object_name = 'auto'
    template_name = 'AppProyecto/autoBorrado.html'
class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionAuto
    success_url = reverse_lazy('autos')
    context_object_name = 'auto'
    template_name = 'AppProyecto/autoEdicion.html'

# VIEWS PARA LAS BICICLETAS
class BicicletaDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaDetalle.html'

class BicicletaLista(LoginRequiredMixin, ListView):
    context_object_name = 'bicicletas'
    queryset = Vendedor.objects.filter(articulo__startswith='bicicleta')
    template_name = 'AppProyecto/listaBicicleta.html'
    login_url = '/login/'
class BicicletaDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaBorrado.html'
class BicicletaUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionBicicleta
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaEdicion.html'

#Para las motos
class MotoDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'moto'
    template_name = 'AppProyecto/motoDetalle.html'

class MotoLista(LoginRequiredMixin, ListView):
    context_object_name = 'motos'
    queryset = Vendedor.objects.filter(articulo__startswith='moto')
    template_name = 'AppProyecto/listaMoto.html'
    login_url = '/login/'
class MotoDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('motos')
    context_object_name = 'moto'
    template_name = 'AppProyecto/motoBorrado.html'
class MotoUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionMoto
    success_url = reverse_lazy('motos')
    context_object_name = 'moto'
    template_name = 'AppProyecto/motoEdicion.html'


# VIEWS PARA LAS BICICLETAS
class BicicletaDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaDetalle.html'

class BicicletaLista(LoginRequiredMixin, ListView):
    context_object_name = 'bicicletas'
    queryset = Vendedor.objects.filter(articulo__startswith='bicicleta')
    template_name = 'AppProyecto/listaBicicleta.html'
    login_url = '/login/'
class BicicletaDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaBorrado.html'
class BicicletaUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionBicicleta
    success_url = reverse_lazy('bicicletas')
    context_object_name = 'bicicleta'
    template_name = 'AppProyecto/bicicletaEdicion.html'

#Para los monopatines
class MonopatinDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'monopatines'
    template_name = 'AppProyecto/monopatinDetalle.html'

class MonopatinLista(LoginRequiredMixin, ListView):
    context_object_name = 'monopatines'
    queryset = Vendedor.objects.filter(articulo__startswith='monopatin')
    template_name = 'AppProyecto/listaMonopatin.html'
    login_url = '/login/'
class MonopatinDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('monopatines')
    context_object_name = 'monopatin'
    template_name = 'AppProyecto/monopatinBorrado.html'
class MonopatinUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionMonopatines
    success_url = reverse_lazy('monopatines')
    context_object_name = 'monopatin'
    template_name = 'AppProyecto/monopatinEdicion.html'

    #varios 
class VariostinDetalle(LoginRequiredMixin, DetailView):   
    model = Vendedor
    context_object_name = 'varios'
    template_name = 'AppProyecto/variosDetalle.html'

class VariosLista(LoginRequiredMixin, ListView):
    context_object_name = 'varios'
    queryset = Vendedor.objects.filter(articulo__startswith='vario')
    template_name = 'AppProyecto/listaVarios.html'
    login_url = '/login/'
class VariosDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('varios')
    context_object_name = 'vario'
    template_name = 'AppProyecto/variosBorrado.html'
class VariosUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    form_class = ActualizacionVarios
    success_url = reverse_lazy('varios')
    context_object_name = 'vario'
    template_name = 'AppProyecto/variosEdicion.html'



























#COMENTARIOS DE LA PAGINA
class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'AppProyecto/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)