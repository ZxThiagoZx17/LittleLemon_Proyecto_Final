from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
    path('api/menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('api/menu/', views.MenuItemView.as_view(), name='menu-list'),
    path('api/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-detail'),
    path('api/bookings/', views.BookingView.as_view(), name='booking-list'),
    path('api/bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
]