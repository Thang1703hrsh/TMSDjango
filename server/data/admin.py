from django.contrib import admin

# Register your models here.

from .models_data import Orders,OrderQuota, OrderBooking, OrderDetail


# class OrderDetail(admin.ModelAdmin):
#     list_display = ['code', 'name']
    
admin.site.register(Orders)
admin.site.register(OrderQuota)
admin.site.register(OrderBooking)
admin.site.register(OrderDetail)
