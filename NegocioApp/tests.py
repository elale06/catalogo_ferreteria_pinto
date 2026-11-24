from unittest.mock import patch

from django.test import SimpleTestCase


class ConsultaSubmissionTests(SimpleTestCase):
	@patch('NegocioApp.views.ConsultaForm')
	def test_customer_can_submit_a_consulta(self, consulta_form_class):
		formulario = consulta_form_class.return_value
		formulario.is_valid.return_value = True
		response = self.client.post('/negocio/', {
			'nombre': 'Cliente de prueba',
			'email': 'cliente@example.com',
			'telefono': '+56912345678',
			'asunto': 'Consulta de stock',
			'mensaje': 'Quisiera conocer disponibilidad.',
		})

		self.assertRedirects(response, '/negocio/')
		formulario.save.assert_called_once_with()
