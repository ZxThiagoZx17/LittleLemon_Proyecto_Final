from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_number', 'comment', 'booking_date']
    
    booking_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        })
    )
    
    