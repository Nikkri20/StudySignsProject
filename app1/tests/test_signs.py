from django.test import TestCase, Client
from django.urls import reverse
from app1.models import Sign, Category

class SignsTests(TestCase):
    def setUp(self):
        self.client = Client()

        Sign.objects.create(
            name="Sign1",
            description="Description of Sign1",
            category="Category1",
            photo="photo1.jpg",
            realObjectPhoto="realObjectPhoto1.jpg"
        )
        Sign.objects.create(
            name="Sign2",
            description="Description of Sign2",
            category="Category2",
            photo="photo2.jpg",
            realObjectPhoto="realObjectPhoto2.jpg"
        )

        Category.objects.create(
            name="Category1",
            description="Description of Category1",
            category="Code1"
        )
        Category.objects.create(
            name="Category2",
            description="Description of Category2",
            category="Code2"
        )

    def test_send_signs(self):
        response = self.client.get(reverse('send_signs'))
        
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 2)

        self.assertIn("1", data)
        self.assertEqual(data["1"]["name"], "Sign1")
        self.assertEqual(data["1"]["description"], "Description of Sign1")
        self.assertEqual(data["1"]["category"], "Category1")
        self.assertEqual(data["1"]["picture"], "/media/photo1.jpg")
        self.assertEqual(data["1"]["pictureWorld"], "/media/realObjectPhoto1.jpg")

        self.assertIn("2", data)
        self.assertEqual(data["2"]["name"], "Sign2")
        self.assertEqual(data["2"]["description"], "Description of Sign2")
        self.assertEqual(data["2"]["category"], "Category2")
        self.assertEqual(data["2"]["picture"], "/media/photo2.jpg")
        self.assertEqual(data["2"]["pictureWorld"], "/media/realObjectPhoto2.jpg")

    def test_send_categories(self):
        response = self.client.get(reverse('send_categories'))
        
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data), 2)

        self.assertIn("1", data)
        self.assertEqual(data["1"]["name"], "Category1")
        self.assertEqual(data["1"]["description"], "Description of Category1")
        self.assertEqual(data["1"]["category"], "Code1")

        self.assertIn("2", data)
        self.assertEqual(data["2"]["name"], "Category2")
        self.assertEqual(data["2"]["description"], "Description of Category2")
        self.assertEqual(data["2"]["category"], "Code2")
