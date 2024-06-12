from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer


class ListcreateSuppliers(generics.ListCreateAPIView):
    queryset = Supplier.objects.prefetch_related('items').order_by('-date_joined')
    serializer_class = SupplierSerializer


class RetrieveUpdateSuppliers(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.prefetch_related('items').all()
    serializer_class = SupplierSerializer
