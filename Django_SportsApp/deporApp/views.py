from django.shortcuts import render
from . import models
from django.utils import timezone
from .forms import DeporteForm, EquipoForm, InstalacionForm, JugadorForm, PartidoForm
from django.views import generic

def inicio(request):
    ultimos_partidos_jugados = models.Partido.objects.filter(fecha_hora__lt=timezone.now()).order_by("-fecha_hora")[:5]
    proximos_partidos = models.Partido.objects.filter(fecha_hora__gt=timezone.now()).order_by("fecha_hora")[:5]

    contexto= {}
    contexto["ultimos"]= ultimos_partidos_jugados
    contexto["proximos"]= proximos_partidos

    return render(request, "inicio.html", contexto)

# Vistas de deportes
class DeporteListView(generic.ListView):
    model = models.Deporte
    template_name = "list_deportes.html"
    context_object_name = "deporte"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CrearDeporteView(generic.CreateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = "crear_deporte.html"
    success_url = "/list_deportes"
    
class BorrarDeporteView(generic.DeleteView):
    model = models.Deporte
    fields = "__all__"
    template_name = "borrar_deporte.html"
    success_url = "/list_deportes"


class ActualizarDeporteView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = "actualizar_deporte.html"
    success_url = "/list_deportes"


# Vistas de equipos
class EquipoListView(generic.ListView):
    model = models.Equipo
    template_name = "list_equipos.html"
    context_object_name = "equipo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CrearEquipoView(generic.CreateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = "crear_equipo.html"
    success_url = "/list_equipos"
    
class BorrarEquipoView(generic.DeleteView):
    model = models.Equipo
    fields = "__all__"
    template_name = "borrar_equipo.html"
    success_url = "/list_equipos"


class ActualizarEquipoView(generic.UpdateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = "actualizar_equipo.html"
    success_url = "/list_equipos"


# Vistas de instalaciones
class InstalacionListView(generic.ListView):
    model = models.Instalacion
    template_name = "list_instalaciones.html"
    context_object_name = "instalacion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BorrarInstalacionView(generic.DeleteView):
    model = models.Instalacion
    fields = "__all__"
    template_name = "borrar_instalacion.html"
    success_url = "/list_instalaciones"


class ActualizarInstalacionView(generic.UpdateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = "actualizar_instalacion.html"
    success_url = "/list_instalaciones"

class CrearInstalacionView(generic.CreateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = "crear_instalacion.html"
    success_url = "/list_instalaciones"
    
# Vistas de jugadores
class JugadorListView(generic.ListView):
    model = models.Jugador
    template_name = "list_jugadores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BorrarJugadorView(generic.DeleteView):
    model = models.Jugador
    fields = "__all__"
    template_name = "borrar_jugador.html"
    success_url = "/list_jugadores"

class ActualizarJugadorView(generic.UpdateView):
    model = models.Jugador
    form_class = JugadorForm
    template_name = "actualizar_jugador.html"
    success_url = "/list_jugadores"

class CrearJugadorView(generic.CreateView):
    model = models.Jugador
    form_class = JugadorForm
    template_name = "crear_jugador.html"
    success_url = "/list_jugadores"
    
# Vistas de Partidos
class PartidoListView(generic.ListView):
    model = models.Partido
    template_name = "list_partidos.html"

    def get_queryset(self):
        # Filtrar y ordenar los partidos por fecha_hora
        queryset = models.Partido.objects.all().order_by("fecha_hora")
        return queryset


class BorrarPartidoView(generic.DeleteView):
    model = models.Partido
    fields = "__all__"
    template_name = "borrar_partido.html"
    success_url = "/list_partidos"

class ActualizarPartidoView(generic.UpdateView):
    model = models.Partido
    form_class = PartidoForm
    template_name = "actualizar_partido.html"
    success_url = "/list_partidos"
    
class CrearPartidoView(generic.CreateView):
    model = models.Partido
    form_class = PartidoForm
    template_name = "crear_partido.html"
    success_url = "/list_partidos"
    
class DetalleJugadorView(generic.DetailView):
    model = models.Jugador
    template_name = "detalle_jugador.html"
    fields = "__all__"
    
class DetallePartidoView(generic.DetailView):
    model = models.Partido
    template_name = "detalle_partido.html"
    fields = "__all__"
    
def detalleViewEquipos(request, pk):
    equipo= models.Equipo.objects.get(id_equipo=pk)

    jugadores= models.Jugador.objects.filter(id_equipo=pk)
    contexto= {}
    contexto["equipo"] = equipo
    contexto["jugadores"] = jugadores

    return render(request, "detalle_equipo.html", contexto)