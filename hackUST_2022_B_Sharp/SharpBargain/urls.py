from django.urls import path
from . import views
urlpatterns = [
    path("index/login_check/",views.login_test,name="login_check"),
    path("index/",views.index,name="index"),
    path("cusHistory/<str:account_address>/",views.cusHistory,name="cusHistory"),
    path("cusComment/<str:account_address>/<int:product_id>/", views.cusComment, name="cusComment"),
    path("cusView/<str:account_address>/<int:product_id>/", views.cusView, name="cusView"),
    path("retailerPOS/<str:account_address>/", views.retailerPOS, name="retailerPOS"),
    path("retailerView/<str:account_address>/", views.retailerView, name="retailerView"),
    path("retailerViewComment/<str:account_address>/<str:prod_type>/", views.retailerViewComment, name="retailerViewComment"),
    path("manuProdInput/", views.manuProdInput, name="manuProdInput"),
    path("manuWS/", views.manuWS, name="manuWS"),
    path("manuView/<str:account_address>/", views.manuView, name="manuView"),
    path("manuViewData/<str:account_address>/<str:prod_type>/", views.manuViewData, name="manuViewData"),

    path("cusDashboard/<str:account_address>/",views.cusDashboard,name="cusDashboard"),
    path("retailerDashboard/<str:account_address>/",views.retailerDashboard,name="retailerDashboard"),
    path("manuDashboard/<str:account_address>/",views.manuDashboard,name="manuDashboard"),
    path("testm/",views.testm,name="testm")





]