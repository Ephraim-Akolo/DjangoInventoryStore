from rest_framework import generics
from .models import Inventory
from .serializers import InventorySerializer


class ListcreateInventoryItems(generics.ListCreateAPIView):
    queryset = Inventory.objects.prefetch_related('suppliers').all().order_by('-created')
    serializer_class = InventorySerializer


class RetrieveUpdateDestroyInventoryItems(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.prefetch_related('suppliers').all()
    serializer_class = InventorySerializer
