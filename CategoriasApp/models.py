from django.db import models
from django.core.validators import MaxValueValidator


class Volumen(models.Model):
	id = models.PositiveIntegerField(
		primary_key=True,
		validators=[MaxValueValidator(999)],
	)
	nombre = models.CharField(max_length=50)
	categoria = models.CharField(max_length=50)
	stock = models.PositiveIntegerField(validators=[MaxValueValidator(999)])

	class Meta:
		ordering = ['id']
		verbose_name = 'Volumen'
		verbose_name_plural = 'Volúmenes'

	def __str__(self):
		return self.nombre


class Precios(models.Model):
	volumen = models.OneToOneField(
		Volumen,
		on_delete=models.CASCADE,
		related_name='precio',
	)
	precio = models.DecimalField(max_digits=10, decimal_places=0)
	moneda = models.CharField(max_length=10, default='CLP')
	observacion = models.CharField(max_length=100, blank=True)

	class Meta:
		ordering = ['volumen__id']
		verbose_name = 'Precio'
		verbose_name_plural = 'Precios'

	def __str__(self):
		return f'{self.volumen} - {self.precio} {self.moneda}'
