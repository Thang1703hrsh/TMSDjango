
from django.contrib import admin
from django.urls import path, include
from data.views import OrderAPIView, OutsourcingProductMaterialsAPIView, OutsourcingProductAPIView
from data import admin_DA, get_purchase_order, get_req_stock_in, get_need_quantity, get_material_reports, get_product_unit, temporary_quantity, views, get_ttd_auth

from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/' , include('djoser.urls')),
    path('api/v1/' , include('djoser.urls.authtoken')),
    path('api/v1/order/' ,  OrderAPIView.as_view()),
    path('api/v1/outsourcing_product_materials/' ,  OutsourcingProductMaterialsAPIView.as_view()),
    path('api/v1/outsourcing_product/' ,  OutsourcingProductAPIView.as_view()),
    # path('' , TemplateView.as_view(template_name = 'index.html')),
    # path("data/productdetail/" , productDetailAPIView.as_view()),
    # path("data/order/" , OrderAPIView.as_view()),
    # path("data/orderdetail/" , OrderDetailAPIView.as_view()),
    # path("data/outsourcing/" , outsourcingProductMaterialsAPIView.as_view()),
    # path("" , temporary_quantity),
    # path("" , get_product_unit),
    # path("" , admin_DA),
    # path("" , get_purchase_order),
    # path("" , getOutsourcing),
    # path("" , get_req_stock_in),
    # path("" , get_need_quantity),
    # path("" , get_material_reports),
]
