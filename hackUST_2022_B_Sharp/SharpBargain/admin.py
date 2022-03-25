from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('prod_type','manu_address')
    list_filter = ('prod_type','manu_address')

admin.site.register(DB_Product)
