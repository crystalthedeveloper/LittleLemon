from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu 
from restaurant.serializers import MenuSerializer

# Create your tests here.
class MenuViewTest(TestCase):
    def setUp(self):
        # Create some test instances of the Menu model
        self.menu_item1 = Menu.objects.create(
            title='Item 1',
            price=9.99,
            inventory=10
        )
        self.menu_item2 = Menu.objects.create(
            title='Item 2',
            price=12.99,
            inventory=5
        )

        # Create an instance of the APIClient
        self.client = APIClient()

    def test_getall(self):
        # Define the URL for the MenuView
        url = reverse('menu-list')  # Replace 'menu-list' with the actual name of your view

        # Perform a GET request to retrieve all Menu items
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the expected data
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2], many=True).data

        # Check if the serialized data in the response equals the expected data
        self.assertEqual(response.data, expected_data)