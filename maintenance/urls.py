from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('maintenances/', views.maintenances, name='maintenances'),
    path('maintenance/<str:pk>/', views.maintenance, name='maintenance_category'),
    path('request/', views.create_request, name='request'),
    path('IT/', views.helpDesk, name='IT'),
]