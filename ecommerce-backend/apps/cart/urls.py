from django.urls import path
from .views import CartListCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),
]