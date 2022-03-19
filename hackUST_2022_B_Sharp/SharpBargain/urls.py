from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('MetaMaskTestPage/', views.MetaMaskTestPage,name="MetaMaskTestPage"),
    path('test/random_url/', views.some_func,name="some_func"),
    path('test/read_name/', views.read_name,name="read_name"),
    path('test/', views.Test,name="test"),


]