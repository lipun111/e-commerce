from django.urls import path, re_path
from home import views

urlpatterns = [
    path('', views.home_View, name='home'),
    path('contact/', views.contact_View, name='contact'),
    path('about/', views.about_View, name='about'),
    path('register/', views.register_view, name='register'),
]
