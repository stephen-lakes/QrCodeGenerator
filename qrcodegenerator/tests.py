from django.test import TestCase

from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomepageViewTest(SimpleTestCase):

    def test_view_url_exist_at_proper_location(self):
        repsonse = self.client.get('/')

        self.assertEqual(repsonse.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_templated(self):
        resp = self.client.get('/')
        
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')


class AboutPageView(SimpleTestCase):

    def test_view_url_exist_at_proper_location(self):
        repsonse = self.client.get('/about/')

        self.assertEqual(repsonse.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('about'))
        
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_templated(self):
        resp = self.client.get('/about/')

        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'about.html')