from django.db import models
from suppliers.models import Supplier
from uuid import uuid4

# Create your models here.


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=3)
    suppliers = models.ManyToManyField(Supplier, with_related='items')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
