from django.db import models

# Create your models here.
class Warehouse(models.Model):
    number=models.CharField( max_length=5,unique=True)
    def __str__(self):
        return self.number

class Category(models.Model):
    category=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.category

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    warehouse=models.ForeignKey(Warehouse,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()

    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
