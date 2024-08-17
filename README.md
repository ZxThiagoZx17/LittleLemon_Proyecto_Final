# LittleLemon_Proyecto_Final
Proyecto final curso Backend META

# :lemon: Little Lemon - Restaurant Reservation and Menu Management :lemon:
## Welcome to the Restaurant Reservation and Menu Management System! This project allows users to explore the restaurant menu, make bookings, and learn more about the restaurant.


### FRONTEND VIEW'S :hear_no_evil:
Home:
    URL: /

About Page:
    URL: /about/

Booking Page:
    URL: /book/

Menu Page:
    URL: /menu/

### BACKEND API Endpoints :rocket:

Menu Items - Retrieve All Menu Items
```
    URL: /api/menu/
    Method: GET
```



Retrieve Specific Menu Item

```
    URL: /api/menu/<int:pk>/
    Method: GET
```



Display Menu Item

```
    URL: /api/menu_item/<int:pk>/
    Method: GET
```



Bookings - Create and List Bookings
```
    URL: /api/bookings/
    Methods: GET, POST
```

Retrieve, Update, and Delete Specific Booking
```
    URL: /api/bookings/<int:pk>/
    Methods: GET, PUT, DELETE
```

## Getting Started :key:
To get a local copy up and running, follow these simple steps.

## Prerequisites
Python 3.x
Django
MySQL




## Installation :gear:

### Clone the repo
git clone https://github.com/ZxThiagoZx17/LittleLemon_Proyecto_Final.git

### Install dependencies from venv.
```
pip install -r requirements.txt
```
or
### Install dependencies from PipEnv
```
pipenv install
```

### Configure your database settings in settings.py.

### Run the migrations

```
python manage.py makemigrations
python manage.py migrate
```

### Start the development server :star:

```
python manage.py runserver
```




## Usage :beginner:
Visit the homepage at http://127.0.0.1:8000/.




## License :warning: 
Distributed under the MIT License. See LICENSE for more information.
