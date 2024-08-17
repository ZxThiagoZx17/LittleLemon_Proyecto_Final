from django.shortcuts import render, redirect
from django.contrib import messages
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from .permissions import IsOwnerOrAdmin, IsAdminOrStaffOrOwner
from .forms import BookingForm
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made successfully!')
            return redirect('book')
        else:
            messages.success(request, 'Your reservation has not been made successfully!')
            return redirect('book')
    else:
        context = {'form':form}
        return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    menu_data = menu_data.order_by('price')
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'POST':    
            permission_classes = [IsOwnerOrAdmin]
        return [permission() for permission in permission_classes]


class MenuItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        print(self.request.user)
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrOwner]
    