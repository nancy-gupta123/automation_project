from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    
    # example fields
    customer = models.CharField(max_length=100, null=True, blank=True)
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # ... other fields


    def __str__(self):
        return f"Order {self.id} - {self.food.name}"
