from django.db import models


class Rol(models.Model):
    descripcion = models.TextField(blank=True)
    nombreRol = models.CharField(max_length=20)


    def __str__(self):
        return self.nombreRol  


class Empleado(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True)
    contraseña = models
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    estado = models.BooleanField
    fotoEmpleado = models.ImageField

    def __str__(self):
        return f"{self.nombre}{self.apellido}"


class RegistroDeAsistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    horaEntrada = models.TimeField(auto_now_add=True)
    horaSalida = models.TimeField (null= True, blank=True)
    detalle = models.CharField(max_length=150)


    def __str__(self):
        return f"Asistencia {self.empleado}{self.fecha}"


class HistorialDeAcceso(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    fechaHora = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Acceso {self.empleado} {self.fechaHora}"