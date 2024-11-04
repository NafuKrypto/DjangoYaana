from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


