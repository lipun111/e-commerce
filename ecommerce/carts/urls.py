from django.urls import path
from carts import views


urlpatterns = [
    path('', views.cart_home_view, name='home'),
    path('update/', views.cart_update, name='update'),
    path('checkout/', views.checkout_view, name='checkout'),
]
