from django.db import models
from pizza.models import PizzaModel
from django.utils.translation import gettext_lazy as _
# Create your models here.

class OrderModel(models.Model):
    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

    class DeliveryStatus(models.TextChoices):
        PENDING = 'PEN', _('Pending')
        DELIVERED = 'DEL', _('Delivered')

    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)
    delivery_status = models.CharField(
        max_length=3, 
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING
    )

    def __str__(self):
        return f'Address: {self.address}, Order: {", ".join([g.name for g in self.pizza_order.all()])}'
    
    def all_orders(self):
        return "\n".join([o.name for o in self.pizza_order.all()])
    
class OrderProxy(OrderModel.pizza_order.through):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.ordermodel)