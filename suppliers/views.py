from rest_framework import generics
from .models import Supplier
from .serializers import SupplierSerializer


class ListcreateSuppliers(generics.ListCreateAPIView):
    queryset = Supplier.objects.all().order_by('-date_joined')
    serializer_class = SupplierSerializer


class RetrieveUpdateSuppliers(generics.RetrieveUpdateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
