from django.db import models

# Create your models here.

class Ingredients(models.Model):

    values= (
        ('liters','Liters'),
        ('pieces','Pieces'),
        ('kilos','Kilos'),
        ('grams','Grams'),
        ('packs','Packs'),
    )
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    quantity_value = models.CharField(max_length=50,choices=values,default='pieces')


    def __str__(self) -> str:
        return f'{self.name} | {self.quantity} {self.quantity_value}'
    

    def save(self,*args, **kwargs):
        self.name = self.name.lower()
        return super(Ingredients,self).save(*args, **kwargs)
    




class FoodRecipes(models.Model):
    name = models.CharField(max_length=100)
    recipe=models.ManyToManyField(Ingredients)
    needed_ings = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    





    
