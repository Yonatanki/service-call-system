from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('maintenances/', views.maintenances, name='maintenances'),
    path('maintenance/<str:pk>/', views.maintenance, name='maintenance_category'),
    path('create_request/', views.create_request, name='create_request'),
    path('request_details/<str:pk>/', views.request_details, name='request_details'),
    path('requests/', views.requests, name='requests'),
    path('IT/', views.helpDesk, name='IT'),
]