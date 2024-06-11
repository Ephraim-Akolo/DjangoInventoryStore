from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer


class ListcreateSupplierItems(generics.ListCreateAPIView):
    queryset = Supplier.objects.all().order_by('-created')
    serializer_class = SupplierSerializer


class RetrieveUpdateInventoryItems(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
