from django.db import models

# Create your models here.
class Comment(models.Model):
    age = models.IntegerField()
    name = models.TextField()
    angl = models.CharField(max_length=4)
    status = models.CharField(max_length=24)
    def __init__(self,age,name,angl):
        allowedLevel = ["B3","B4"]
        self.age = age
        self.name = name
        self.angl = angl
        self.status = "Принят" if self.angl in allowedLevel and self.age > 25 else "Не принят"

class Product():
    def __init__(self,name,color,weight,price,discount):
        self.name = name
        self.color = color
        self.weight = weight
        self.discount = discount
        self.price = price*0.9 if discount else price

