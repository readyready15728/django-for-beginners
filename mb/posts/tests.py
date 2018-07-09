from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    message = 'Just a test'

    def setUp(self):
        Post.objects.create(text=self.message)
    def test_text_contest(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, self.message)

class HomePageViewTest(TestCase):
    message = 'Another test'

    def setUp(self):
        Post.objects.create(text=self.message)
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
