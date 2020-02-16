from django.urls import path, re_path
from products import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='list'),
    # path('product/<int:pk>/', views.product_details_view, name='details'),
    re_path('(?P<slug>[-\w]+)/', views.product_details_slug_view.as_view(), name='details'),
]
