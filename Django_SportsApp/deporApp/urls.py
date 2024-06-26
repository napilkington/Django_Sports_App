from django.urls import include, path
from . import views
from django.contrib import admin


app_name = "deporApp"

urlpatterns = [
    path('', views.inicio, name="inicio"),
     path('deporApp/', views.inicio, name="inicio"),
    # Deportes
    path('list_deportes/', views.DeporteListView.as_view(), name="list_deportes"),
    path('borrar_deporte/<int:pk>/', views.BorrarDeporteView.as_view(), name="borrar_deporte"),
    path('actualizar_deporte/<int:pk>/', views.ActualizarDeporteView.as_view(), name="actualizar_deporte"),
    path('crear_deporte/', views.CrearDeporteView.as_view(), name="crear_deporte"),
    
    # Equipos
    path('list_equipos/', views.EquipoListView.as_view(), name="list_equipos"),
    path('borrar_equipo/<int:pk>/', views.BorrarEquipoView.as_view(), name="borrar_equipo"),
    path('actualizar_equipo/<int:pk>/', views.ActualizarEquipoView.as_view(), name="actualizar_equipo"),
    path('crear_equipo/', views.CrearEquipoView.as_view(), name="crear_equipo"),
    # path('detalle_equipo/<int:pk>/', views.DetalleEquipoView.as_view(), name="detalle_equipo"),
    path('detalle_equipo/<int:pk>/', views.detalleViewEquipos, name="detalle_equipo"),
    # Instalaciones
    path('list_instalaciones/', views.InstalacionListView.as_view(), name="list_instalaciones"),
    path('borrar_instalacion/<int:pk>/', views.BorrarInstalacionView.as_view(), name="borrar_instalacion"),
    path('actualizar_instalacion/<int:pk>/', views.ActualizarInstalacionView.as_view(), name="actualizar_instalacion"),
    path('crear_instalacion/', views.CrearInstalacionView.as_view(), name="crear_instalacion"),
    # Jugadores
    path('list_jugadores/', views.JugadorListView.as_view(), name="list_jugadores"),
    path('borrar_jugador/<int:pk>/', views.BorrarJugadorView.as_view(), name="borrar_jugador"),
    path('actualizar_jugador/<int:pk>/', views.ActualizarJugadorView.as_view(), name="actualizar_jugador"),
    path('crear_jugador/', views.CrearJugadorView.as_view(), name="crear_jugador"),
    path('detalle_jugador/<int:pk>/', views.DetalleJugadorView.as_view(), name="detalle_jugador"),
    # Partidos
    path('list_partidos/', views.PartidoListView.as_view(), name="list_partidos"),
    path('borrar_partido/<int:pk>/', views.BorrarPartidoView.as_view(), name="borrar_partido"),
    path('actualizar_partido/<int:pk>/', views.ActualizarPartidoView.as_view(), name="actualizar_partido"),
    path('crear_partido/', views.CrearPartidoView.as_view(), name="crear_partido"),
    path('detalle_partido/<int:pk>/', views.DetallePartidoView.as_view(), name="detalle_partido"),
]