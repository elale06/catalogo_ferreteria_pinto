from django.test import SimpleTestCase
from django.urls import resolve, reverse
from django.core.exceptions import PermissionDenied
from django.test import RequestFactory
from django.template import engines
from types import SimpleNamespace

from .api_views import IsAdminOrReadOnly
from .views import RoleBasedLoginView
from PrincipalApp.admin import admin_site


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

	def test_login_page_is_available(self):
		response = self.client.get(reverse('categorias:login'))
		self.assertEqual(response.status_code, 200)

	def test_staff_cannot_open_crud_routes(self):
		request = RequestFactory().get('/categorias/acceso/')
		request.user = SimpleNamespace(is_authenticated=True, is_superuser=False)
		view = resolve('/categorias/acceso/').func

		with self.assertRaises(PermissionDenied):
			view(request)

	def test_staff_cannot_open_user_creation(self):
		request = RequestFactory().get('/categorias/usuarios/crear/')
		request.user = SimpleNamespace(is_authenticated=True, is_superuser=False)
		view = resolve('/categorias/usuarios/crear/').func

		with self.assertRaises(PermissionDenied):
			view(request)

	def test_staff_can_read_api_but_cannot_write(self):
		permission = IsAdminOrReadOnly()
		staff_user = SimpleNamespace(is_authenticated=True, is_superuser=False)

		for method, expected in (('GET', True), ('POST', False), ('PATCH', False), ('DELETE', False)):
			with self.subTest(method=method):
				request = SimpleNamespace(method=method, user=staff_user)
				self.assertEqual(permission.has_permission(request, None), expected)

	def test_only_admin_can_access_django_backoffice(self):
		staff_request = SimpleNamespace(user=SimpleNamespace(is_active=True, is_superuser=False))
		admin_request = SimpleNamespace(user=SimpleNamespace(is_active=True, is_superuser=True))

		self.assertFalse(admin_site.has_permission(staff_request))
		self.assertTrue(admin_site.has_permission(admin_request))

	def test_admin_can_write_to_api(self):
		permission = IsAdminOrReadOnly()
		admin_user = SimpleNamespace(is_authenticated=True, is_superuser=True)
		request = SimpleNamespace(method='POST', user=admin_user)

		self.assertTrue(permission.has_permission(request, None))

	def test_login_redirects_staff_home_and_admin_to_management(self):
		view = RoleBasedLoginView()
		view.request = SimpleNamespace(user=SimpleNamespace(is_superuser=False))
		self.assertEqual(view.get_success_url(), '/')

		view.request = SimpleNamespace(user=SimpleNamespace(is_superuser=True))
		self.assertEqual(view.get_success_url(), '/categorias/acceso/')

	def test_navigation_shows_the_icon_for_each_role(self):
		template = engines['django'].from_string(
			"{% include 'nav_principal.html' %}"
		)
		request = SimpleNamespace(path='/')
		for user, icon in (
			(SimpleNamespace(is_authenticated=True, is_staff=True, is_superuser=False, get_username=lambda: 'staff'), 'staff.png'),
			(SimpleNamespace(is_authenticated=True, is_staff=True, is_superuser=True, get_username=lambda: 'admin'), 'admin.png'),
		):
			with self.subTest(icon=icon):
				rendered = template.render({'user': user, 'request': request})
				self.assertIn(f'iconos_usuarios/{icon}', rendered)
