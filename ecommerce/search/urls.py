from django.urls import path, re_path
from search import views


urlpatterns = [
    path('', views.SearchProductView.as_view(), name='query'),
]
