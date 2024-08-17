# restaurant/tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, BookingSerializer

class MenuTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.menu_item = Menu.objects.create(name='Burger', price=10.0, description='A delicious burger')
        self.menu_item2 = Menu.objects.create(name='Pizza', price=20.0, description='A cheesy pizza')

    def test_menu_list(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_menu_create(self):
        url = reverse('menu-list')
        data = {'name': 'Salad', 'price': 5.0, 'description': 'A healthy salad'}
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(Menu.objects.get(pk=response.data['id']).name, 'Salad')
    
    def test_menu_update(self):
        url = reverse('menu-detail', args=[self.menu_item.pk])
        data = {'name': 'Updated Burger', 'price': 15.0, 'description': 'An updated delicious burger'}
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(url, data, format='json')
        self.menu_item.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.menu_item.name, 'Updated Burger')
    
    def test_menu_delete(self):
        url = reverse('menu-detail', args=[self.menu_item.pk])
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)

class BookingTests(APITestCase):
    
    def create(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.booking = Booking.objects.create(
            first_name='John',
            last_name='Doe',
            guest_number=4,
            comment='No comment',
            booking_date='2024-07-22T15:00:00Z'
        )
