from rest_framework import serializers
from .models import Inventory
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
from decimal import Decimal


class InventorySerializer(serializers.ModelSerializer):
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='suppliers', many=True, write_only=True)
    price = serializers.DecimalField(min_value=Decimal(0), max_digits=12, decimal_places=2)

    class Meta(object):
        model = Inventory
        fields = '__all__'