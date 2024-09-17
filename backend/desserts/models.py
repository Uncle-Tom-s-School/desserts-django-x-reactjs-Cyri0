from django.db import models

# Create your models here.

class DessertCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(DessertCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to="assets/images/")

    def __str__(self):
        return self.name