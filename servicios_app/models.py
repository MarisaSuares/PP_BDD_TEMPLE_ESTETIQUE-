from django.db import models

class Servicio(models.Model):
    nombreServicio = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombreServicio


class ServicioRealizado(models.Model):
    empleado = models.ForeignKey(
        "empleados_app.Empleado", 
        on_delete=models.PROTECT,
        related_name="servicios_realizados"
    )
    servicio = models.ForeignKey(
        Servicio, 
        on_delete=models.PROTECT,
        related_name="servicios_realizados"
    )
    registroMensual = models.ForeignKey(
        "liquidaciones_app.RegistroMensual", 
        on_delete=models.PROTECT,
        related_name="servicios_realizados",
        null=True,
        blank=True
    )

    fecha = models.DateTimeField(auto_now_add=True)
    montoServicio = models.DecimalField(max_digits=10, decimal_places=2)
    porcentajeEmpleado = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Servicio Realizado"
        verbose_name_plural = "Servicios Realizados"

    def __str__(self):
        return f"{self.servicio.nombreServicio} por {self.empleado} - {self.fecha.strftime('%d/%m/%Y')}"