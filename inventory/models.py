from django.db import models
from suppliers.models import Supplier
from uuid import uuid4

# Create your models here.


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    suppliers = models.ManyToManyField(Supplier, related_name='items')
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return self.name
