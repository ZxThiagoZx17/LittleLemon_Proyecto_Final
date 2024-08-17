# restaurant/tests/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu
from django.utils import timezone

class BookingModelTest(TestCase):
    
    def setUp(self):
        """
        Crear una instancia de User y Booking para usarla en las pruebas.
        """
        self.user = User.objects.create_user(username="testuser", password="password")
        self.booking = Booking.objects.create(
            first_name="John",
            last_name="Doe",
            guest_number=4,
            comment="No comment",
            booking_date=timezone.now()
        )
    
    def test_booking_str_method(self):
        """
        Verificar el método __str__ del modelo Booking.
        """
        expected_str = f"{self.booking.first_name} - {self.booking.booking_date}"
        self.assertEqual(str(self.booking), expected_str)
    
    def test_booking_fields(self):
        """
        Verificar los campos del modelo Booking.
        """
        self.assertEqual(self.booking.first_name, "John")
        self.assertEqual(self.booking.last_name, "Doe")
        self.assertEqual(self.booking.guest_number, 4)
        self.assertEqual(self.booking.comment, "No comment")
        self.assertIsNotNone(self.booking.booking_date)

class MenuModelTest(TestCase):
    
    def setUp(self):
        """
        Crear una instancia de Menu para usarla en las pruebas.
        """
        self.menu_item = Menu.objects.create(
            name="Burger",
            price=10,
            description="A delicious burger"
        )
    
    def test_menu_str_method(self):
        """
        Verificar el método __str__ del modelo Menu.
        """
        self.assertEqual(str(self.menu_item), "Burger")
    
    def test_menu_fields(self):
        """
        Verificar los campos del modelo Menu.
        """
        self.assertEqual(self.menu_item.name, "Burger")
        self.assertEqual(self.menu_item.price, 10)
        self.assertEqual(self.menu_item.description, "A delicious burger")
