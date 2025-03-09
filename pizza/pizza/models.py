from django.db import models

# Create your models here.
class ToppingsModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Toppings'
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return self.name
    
class PizzaModel(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(ToppingsModel, verbose_name='toppings')

    class Meta:
        verbose_name = 'My pizza recipes'
        verbose_name_plural = 'Pizza recipes'

    def __str__(self):
        return f'{self.name} : {", ".join([topping.name for topping in self.toppings.all()])}'
    
    def all_toppings(self):
        return "\n".join([t.name for t in self.toppings.all()])
    
class PizzaProxy(PizzaModel.toppings.through):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.toppingsmodel)