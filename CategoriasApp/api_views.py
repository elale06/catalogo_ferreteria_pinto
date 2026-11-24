from rest_framework import viewsets
from .models import Precios, Volumen
from .serializers import PreciosSerializer, VolumenSerializer

class VolumenViewSet(viewsets.ModelViewSet):
	queryset = Volumen.objects.select_related('precio').all()
	serializer_class = VolumenSerializer

class PreciosViewSet(viewsets.ModelViewSet):
	queryset = Precios.objects.select_related('volumen').all()
	serializer_class = PreciosSerializer
