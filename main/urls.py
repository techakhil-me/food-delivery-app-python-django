from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("cart", views.cart, name='cart'),
    path("login", views.signin, name='signin'),
    path("logout/", views.logout_auth, name="logout_auth"),
]
