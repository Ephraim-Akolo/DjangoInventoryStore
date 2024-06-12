from rest_framework import serializers
from .models import Inventory
from suppliers.models import Supplier
from decimal import Decimal

class InventorySupplierSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Supplier
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    suppliers = InventorySupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='suppliers', many=True, write_only=True)
    price = serializers.DecimalField(min_value=Decimal(0), max_digits=12, decimal_places=2)

    class Meta(object):
        model = Inventory
        fields = '__all__'