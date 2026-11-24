from rest_framework import permissions, viewsets
from .models import Precios, Volumen
from .serializers import PreciosSerializer, VolumenSerializer


class IsAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return (
			request.method in permissions.SAFE_METHODS
			or bool(request.user and request.user.is_authenticated and request.user.is_superuser)
		)


class VolumenViewSet(viewsets.ModelViewSet):
	queryset = Volumen.objects.select_related('precio').all()
	serializer_class = VolumenSerializer
	permission_classes = (IsAdminOrReadOnly,)

class PreciosViewSet(viewsets.ModelViewSet):
	queryset = Precios.objects.select_related('volumen').all()
	serializer_class = PreciosSerializer
	permission_classes = (IsAdminOrReadOnly,)
