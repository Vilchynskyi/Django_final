from django.urls import path
from .views import (
    CartView,
    AddCartView,
    RemoveCartView,
    ClearCartView,
    CheckoutView
)

app_name = 'order'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<pk>/', AddCartView.as_view(), name='cart-add'),
    path('remove/<pk>/', RemoveCartView.as_view(), name='cart-remove'),
    path('clear/', ClearCartView.as_view(), name='cart-clear'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]

