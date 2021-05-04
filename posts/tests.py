from django.test import TestCase

# Create your tests here.
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a test")
    
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_obj_name = f"{post.text}"
        self.assertEqual(expected_obj_name, "Just a test")


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="This is another test")
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code,200)

    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse("home"))  # looking at posts > urls.py name="home"
        self.assertEqual(resp.status_code, 200)

    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")