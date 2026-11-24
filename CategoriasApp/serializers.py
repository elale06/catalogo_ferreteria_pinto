from rest_framework import serializers

from .models import Precios, Volumen


class PreciosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Precios
		fields = ('id', 'volumen', 'precio', 'moneda', 'observacion')


class VolumenSerializer(serializers.ModelSerializer):
	precio_detalle = PreciosSerializer(source='precio', read_only=True)

	class Meta:
		model = Volumen
		fields = ('id', 'nombre', 'categoria', 'stock', 'precio_detalle')
