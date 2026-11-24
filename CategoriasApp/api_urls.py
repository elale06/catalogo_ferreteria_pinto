from rest_framework.routers import DefaultRouter

from .api_views import PreciosViewSet, VolumenViewSet

router = DefaultRouter()
router.register('productos', VolumenViewSet, basename='api-producto')
router.register('precios', PreciosViewSet, basename='api-precio')

urlpatterns = router.urls
