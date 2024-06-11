from rest_framework import serializers
from .models import Inventory
from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer


class InventorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    suppliers = SupplierSerializer(many=True, read_only=True)
    supplier_ids = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), source='suppliers', many=True, write_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta(object):
        model = Inventory
        fields = '__all__'