from django.db import models
from uuid import uuid4

# Create your models here.

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(blank=True)
    other_contact_info = models.TextField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return self.name
