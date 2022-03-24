from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('MetaMaskTestPage/', views.MetaMaskTestPage,name="MetaMaskTestPage"),
    path('test/random_url/', views.some_func,name="some_func"),
    path('test/read_name/', views.read_name,name="read_name"),
    path('test/change_name/', views.read_name,name="change_name"),
    path('test/', views.Test,name="test"),
    path("index/login_check/",views.login_test,name="login_check"),
    path("index/",views.index,name="index"),

    path("cusDashboard/",views.cusDashboard,name="cusDashboard"),
    path("retailerDashboard/",views.retailerDashboard,name="retailerDashboard"),
    path("manuDashboard/",views.manuDashboard,name="manuDashboard"),
    path("testm/",views.testm,name="testm")



]