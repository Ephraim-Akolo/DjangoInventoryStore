from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField(allow_blank=True)
    mobile_number = serializers.CharField(max_length=14, allow_blank=True)
    address = serializers.CharField(allow_blank=True)
    other_contact_info = serializers.CharField(allow_blank=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta(object):
        model = Supplier
        fields = '__all__'
