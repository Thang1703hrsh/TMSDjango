from rest_framework import serializers

from .models_data import *
from .models_auth import *
from .models_report import *


class orderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'
        
class orderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'
        
class productDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'
        
        
class orderBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBooking
        fields = '__all__'
        
        
class ordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class orderBookingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBookingStatus
        fields = '__all__'
                
# class orderQuotaSerializer(serializers.ModelSerializer):
#     code = productDetailSerializer(source='ProductDetail')
#     status = orderStatusSerializer(source='OrderStatus')
#     status = orderBookingStatusSerializer(source='ProductDetail')
#     is_complete = orderDetailSerializer(source='OrderDetail')
    
    
#     class Meta:
#         model = OrderQuota
#         fields = ['id' , 'order_id', 'product_id' , 'code' , 'status' , 'position' , 'total_quota' , 'is_complete']
        
        
class outsourcingProductMaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutsourcingProductMaterials
        fields = ['outsourcing_product_id' , 'product_id']
        