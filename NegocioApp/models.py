from django.db import models


class Consulta(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField()
	telefono = models.CharField(max_length=30, blank=True)
	asunto = models.CharField(max_length=120)
	mensaje = models.TextField()
	creada_en = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-creada_en',)
		verbose_name = 'Consulta de cliente'
		verbose_name_plural = 'Consultas de clientes'

	def __str__(self):
		return f'{self.asunto} - {self.nombre}'
