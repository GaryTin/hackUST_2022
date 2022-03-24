from django.db import models


# Create your models here.
class DB_user(models.Model):
    user_id = models.IntegerField(unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    ROLE_CHOICE = [
        ('C', 'Customer'),
        ('R', 'Retailer'),
        ('M', 'Manufacturer'),
    ]

    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICE,
        default='C'
    )

    name = models.CharField(max_length=256)

    objects = models.Manager()

class DB_Product(models.Model):
    prod_type = models.CharField(max_length=256)
    prod_img = models.ImageField(upload_to="images")

    objects = models.Manager()



class Manufacturer(models.Model):
    manu_id = models.IntegerField(unique=True)
    manu_name = models.CharField(max_length=256)
    manu_address = models.CharField(max_length=256)

    objects = models.Manager()


