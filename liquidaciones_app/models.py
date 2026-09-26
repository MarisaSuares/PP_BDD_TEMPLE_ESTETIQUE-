from django.db import models

class RegistroMensual(models.Model):
    mes = models.IntegerField()
    anio = models.IntegerField()
    totalGenerado = models.DecimalField(max_digits=10, decimal_places=2)
    totalPorcentaje = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = "Registro Mensual"
        verbose_name_plural = "Registros Mensuales "


    def __str__(self):
        return f"Registro Mensual {self.mes}/{self.anio}"


class Aguinaldo(models.Model):
    registroMensual = models.ForeignKey(RegistroMensual, 
        on_delete=models.PROTECT, 
        related_name="aguinaldos")
    periodo = models.CharField(max_length=50)
    montoAguinaldo = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = "Aguinaldo"
        verbose_name_plural  = "Aguinaldos"


    def __str__(self):
        return f"Aguinaldo {self.periodo} - $ {self.montoAguinaldo}"


