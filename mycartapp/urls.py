from django.urls import path
from . views import add_to_cart, cart_detail, update_cart_item

urlpatterns = [
    path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('update_cart_item/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('cart/', cart_detail, name='cart_detail'),
]
