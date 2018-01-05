from django.test import TestCase

# Create your tests here.

class ViewTests(TestCase):
	def test_index_view(self):
		response = self.client.get('')
		# check reponse and template
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')
