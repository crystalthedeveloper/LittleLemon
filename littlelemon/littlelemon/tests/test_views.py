from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model
        Menu.objects.create(title='Dish1', price=10.99, inventory=20)
        Menu.objects.create(title='Dish2', price=15.99, inventory=15)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse('menu-list')  # Assuming 'menu-list' is the name of your API endpoint
        response = client.get(url, format='json')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the test instances
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)