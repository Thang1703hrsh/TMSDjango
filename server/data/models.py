# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    po = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    tolerance = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    loss_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    started_at = models.DateField(blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_pattern_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    tax_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    debit_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_complete = models.IntegerField()
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    vnd_exchange = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_detail'



class OrderQuota(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    loss_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_type = models.CharField(max_length=255, blank=True, null=True)
    total_quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_booking_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_quota'


class OrderBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_booking'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_type = models.CharField(max_length=45, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    tracking_order_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    tracking_order_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'orders'



class ProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    reserve_quantity = models.DecimalField(max_digits=24, decimal_places=10)
    leak_time = models.FloatField()
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    product_type_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_color_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_specification_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    short_code = models.CharField(max_length=10, blank=True, null=True)
    is_outsourcing = models.IntegerField()
    gallery_id = models.BigIntegerField(blank=True, null=True)
    default_img = models.BigIntegerField(blank=True, null=True)
    in_trash = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'product_detail'



# class MaterialReports(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     product_id = models.PositiveBigIntegerField(blank=True, null=True)
#     product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
#     need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     is_calculated = models.IntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'material_reports'

class OutsourcingProductMaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    report_product_need_id = models.PositiveBigIntegerField(blank=True, null=True)
    report_primary_product_need_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_product_materials'


class MaterialReportHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_report_history'


# class MaterialReports(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     product_id = models.PositiveBigIntegerField(blank=True, null=True)
#     product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
#     need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     is_calculated = models.IntegerField()
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
#     temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'material_reports'
