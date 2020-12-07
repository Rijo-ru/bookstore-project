from django.test import SimpleTestCase
from django.urls import reverse

from .views import HomePageView

class HomepageTests(SimpleTestCase):

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        respose = self.client.get('/')
        self.assertTemplateUsed(respose, 'home.html')

    def test_homepage_contains_correct_html(self):
        respose = self.client.get('/')
        self.assertContains(respose, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
