from django.db import models
from django.core.validators import MinValueValidator


# Tabla deportes
class Deporte(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Deporte"
        verbose_name_plural = "Deportes"
        db_table = "deportes"

    def __str__(self):
        return f"{self.nombre}"


# Tabla equipos
class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)
    id_deporte = models.ForeignKey(
        Deporte, on_delete=models.RESTRICT, db_column="id_deporte", default=0
    )
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipos"

    def __str__(self):
        return f"{self.nombre}"


# Tabla instalaciones
class Instalacion(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Instalacion"
        verbose_name_plural = "Instalaciones"
        db_table = "instalaciones"

    def __str__(self):
        return f"{self.nombre}"


# Tabla partidos
class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    id_deporte = models.ForeignKey(
        Equipo, on_delete=models.RESTRICT, db_column="id_deporte", default=0
    )
    fecha_hora = models.DateTimeField()
    id_instalacion = models.ForeignKey(
        Instalacion, on_delete=models.RESTRICT, db_column="id_instalacion", default=0
    )
    id_local = models.ForeignKey(
        Equipo,
        related_name="partidos_local",
        on_delete=models.RESTRICT,
        db_column="id_local",
    )
    id_visitante = models.ForeignKey(
        Equipo,
        related_name="partidos_visitante",
        on_delete=models.RESTRICT,
        db_column="id_visitante",
    )
    puntos_local = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    puntos_visitante = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        db_table = "partidos"

    def __str__(self):
        return f"{self.id_deporte.nombre} {self.id_instalacion.nombre} {self.id_local.nombre} {self.id_visitante.nombre}"



# Tabla jugadores
class Jugador(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20)
    id_equipo = models.ForeignKey(
        Equipo, on_delete=models.RESTRICT, db_column="id_equipo", default=0
    )
    dorsal = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(
        max_digits=3, decimal_places=2, default=0, validators=[MinValueValidator(0)]
    )
    peso = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    telefono = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugadores"

    def __str__(self):
        return f"{self.id_equipo.nombre}"

