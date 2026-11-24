from django.test import SimpleTestCase
from django.urls import reverse


class CrudAuthenticationTests(SimpleTestCase):
	def test_management_routes_redirect_anonymous_users_to_login(self):
		protected_paths = (
			'/categorias/acceso/',
			'/categorias/productos/',
			'/categorias/productos/crear/',
			'/categorias/productos/123/actualizar/',
			'/categorias/productos/123/eliminar/',
		)

		for path in protected_paths:
			with self.subTest(path=path):
				response = self.client.get(path)
				self.assertEqual(response.status_code, 302)
				self.assertTrue(response.url.startswith('/categorias/login/?next='))

	def test_api_rejects_anonymous_writes(self):
		response = self.client.post(
			'/api/productos/',
			data={'id': 123, 'nombre': 'Producto de prueba', 'categoria': 'Prueba', 'stock': 1},
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 403)

	def test_authentication_pages_are_available(self):
		for route_name in ('categorias:registro', 'categorias:login'):
			with self.subTest(route_name=route_name):
				response = self.client.get(reverse(route_name))
				self.assertEqual(response.status_code, 200)
