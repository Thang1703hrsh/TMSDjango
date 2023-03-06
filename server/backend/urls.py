
from django.contrib import admin
from django.urls import path, include
from data.views import OrderAPIView, OutsourcingProductMaterialsAPIView, OutsourcingProductAPIView
from data import admin_DA, get_purchase_order, get_req_stock_in, get_need_quantity, get_material_reports, get_product_unit
from data import  temporary_quantity, views, get_ttd_auth, get_req_stock_out, get_product, get_manufacture_depth, get_manufacture_task, get_manufacture_prod
from data import get_manufacture_product_export, get_order, get_production_tracking, get_production_not_exist_order, get_working_time, get_customers
from data import get_manufacture_product_import, get_manufacture_product_warehouse, get_currency

from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/' , include('djoser.urls')),
    path('api/v1/' , include('djoser.urls.authtoken')),
    path('api/v1/order/' ,  OrderAPIView.as_view()),
    path('api/v1/outsourcing_product_materials/' ,  OutsourcingProductMaterialsAPIView.as_view()),
    path('api/v1/outsourcing_product/' ,  OutsourcingProductAPIView.as_view()),
    path("" , get_manufacture_depth),
    path("" , get_manufacture_task),
    path("" , get_manufacture_prod),
    path("" , get_manufacture_product_export),
    path("" , get_manufacture_product_import),
    path("" , get_order),
    path("" , get_production_tracking),
    path("" , get_production_not_exist_order),
    path("" , get_working_time),
    path("" , get_customers),
    path("" , get_manufacture_product_warehouse),
    path("" , get_purchase_order),
    path("" , get_currency),


    # path('' , TemplateView.as_view(template_name = 'index.html')),
    # path("data/productdetail/" , productDetailAPIView.as_view()),
    # path("data/order/" , OrderAPIView.as_view()),
    # path("data/orderdetail/" , OrderDetailAPIView.as_view()),
    # path("data/outsourcing/" , outsourcingProductMaterialsAPIView.as_view()),
    # path("" , temporary_quantity),
    # path("" , get_product_unit),
    # path("" , admin_DA),
    
    # path("" , getOutsourcing),
    # path("" , get_req_stock_in),
    # path("" , get_need_quantity),
    # path("" , get_material_reports),
    # path("" , get_req_stock_out),
    # path("" , get_product),
]
