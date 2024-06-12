from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True)
    mobile_number = serializers.CharField(max_length=14, allow_blank=True)
    address = serializers.CharField(allow_blank=True)
    other_contact_info = serializers.CharField(allow_blank=True)

    class Meta(object):
        model = Supplier
        fields = '__all__'
