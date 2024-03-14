from django.test import TestCase
from django.http import HttpRequest
from oc_lettings_site.views import handler404, handler500


class ErrorViewsTestCase(TestCase):

    def test_handler404(self):
        request = HttpRequest()
        response = handler404(request, Exception())
        self.assertEqual(response.status_code, 404)
        self.assertIn('Error 404', response.content.decode('utf-8'))

    def test_handler500(self):
        request = HttpRequest()
        response = handler500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn('Error 500', response.content.decode('utf-8'))
