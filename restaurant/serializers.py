from rest_framework.serializers import ModelSerializer, FloatField, CharField
from django.contrib.auth.models import User
from .models import Menu, Booking



class MenuSerializer(ModelSerializer):
    price = FloatField()

    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'description']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'first_name', 'last_name', 'guest_number', 'comment', 'booking_date']