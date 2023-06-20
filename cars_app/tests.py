from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Cars
from django.contrib.auth import get_user_model


# Create your tests here.
class CarsTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("cars_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("cars_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "cars/cars-list.html")
        self.assertTemplateUsed(response, "_base.html")

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test", email="teas@email.com", password="1234"
        )

        self.cars = Cars.objects.create(
            name="test", desc="test info", purchaser=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.cars), "test")

    def test_detail_view(self):
        url = reverse("cars_detail", args=[self.cars.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, "cars/cars-detail.html")

    def test_create_view(self):
        obj = {
            "name": "test2",
            "desc": "info...",
            "purchaser": self.user.id,
        }

        url = reverse("cars_create")
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse("cars_detail", args=[2]))
