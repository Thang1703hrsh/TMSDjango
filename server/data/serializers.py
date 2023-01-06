from rest_framework import serializers

from .models import *

class orderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class productDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
        
                
class orderQuotaSerializer(serializers.ModelSerializer):
    name = orderDetailSerializer(source='OrderDetail')
    product_id = productDetailSerializer(source='ProductDetail')
    class Meta:
        model = OrderQuota
        fields = ['name' , 'position', 'product_id']
        