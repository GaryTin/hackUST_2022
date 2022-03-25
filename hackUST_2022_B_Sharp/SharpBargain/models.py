from django.db import models


# Create your models here.
class DB_Product(models.Model):
    prod_type = models.CharField(max_length=256)
    manu_address = models.CharField(max_length=40)
    prod_img = models.ImageField(upload_to="images")

    objects = models.Manager()




