from django.test import TestCase
from django.urls import reverse
from mysite.apps.webapp.models import *

# Create your tests here.



class AnimalTestCase(TestCase):
    def setUp(self):
        Litigation.objects.create(title="Law", description="Hello")

    def test_text_content(self):
        obj = Litigation.objects.get(id=1)
        expected_object_name = f'{obj.title}'
        self.assertEquals(expected_object_name, 'Law')

    def test_post_list_view(self):
        response = self.client.get(reverse('webapp:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Law')
        self.assertTemplateUsed(response, 'home.html')