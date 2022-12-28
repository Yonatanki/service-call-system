from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),

    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('home/', views.userHome, name="user-home"),
    path('account/', views.userAccount, name="account"),

    # path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    # path('account/', views.home, name="account"),

    # path('customer/', views.customer, name="customer"),
    path('', views.customers, name="customers"),
]