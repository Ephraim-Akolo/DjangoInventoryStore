from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Supplier
from inventory.models import Inventory


class SupplierInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'description', 'price', 'created']


class SupplierSerializer(serializers.ModelSerializer):
    mobile_number = serializers.CharField(max_length=14, validators=[RegexValidator(regex=r'^\+?\d{10,14}$', message="Mobile number must be between 10 and 14 digits.", code='invalid_mobile_number')])
    address = serializers.CharField(allow_blank=True)
    other_contact_info = serializers.CharField(allow_blank=True)
    supplies = serializers.SerializerMethodField()

    class Meta(object):
        model = Supplier
        fields = '__all__'

    def get_supplies(self, obj) -> dict:
        inventories = Inventory.objects.filter(suppliers=obj)
        return SupplierInventorySerializer(inventories, many=True).data

