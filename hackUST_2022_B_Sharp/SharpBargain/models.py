from django.db import models


# Create your models here.
class DB_Product(models.Model):
    prod_type = models.CharField(max_length=256)
    prod_img = models.ImageField(upload_to="images")

    objects = models.Manager()

    def __str__(self):
        return (self.prod_type)




