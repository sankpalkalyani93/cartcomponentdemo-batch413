from django.urls import path
from . views import add_to_cart, cart_detail, update_cart_item, remove_from_cart

urlpatterns = [
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart_item/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
]
