# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssignImportOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    req_stockin_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    packing_list_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_import_order'


class AssignOutsourcingOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_outsourcing_order'


class AssignProductStockout(models.Model):
    id = models.BigAutoField(primary_key=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sp_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    sp_order_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_order_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_quota_id = models.PositiveBigIntegerField(blank=True, null=True)
    return_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    return_product_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    req_stockout_prod_id = models.PositiveBigIntegerField(blank=True, null=True)
    req_stockout_prod_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    mat_offset_production_id = models.PositiveBigIntegerField(blank=True, null=True)
    mat_offset_production_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_product_stockout'


class AssignProductionManufactureDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    production_department_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_production_manufacture_department'


class AssignReqChangePrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_change_price_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    product_stock_real_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_req_change_prices'


class AssignSupplierCredits(models.Model):
    id = models.BigAutoField(primary_key=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    supplier_credit_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_supplier_credits'


class AssignSupplierDebits(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_debit_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    supplier_debit_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_supplier_debits'


class AssignSupplierReduces(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_reduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_supplier_reduces'


class Bills(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField()
    order_type = models.CharField(max_length=255, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField()
    customer_id = models.PositiveBigIntegerField()
    media_id = models.PositiveBigIntegerField()
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bills'


class ChangeMaterialDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_change_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    loss_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_type = models.CharField(max_length=255, blank=True, null=True)
    total_quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_material_detail'


class CreditDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    invoice_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    customer_bank_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_detail'


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency'


class CurrencyDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    symbol = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_details'


class CurrencyExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    source_currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    result_currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    source_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    result_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_exchange'


class CusProductionProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus_production_process'


class CusProductionSetting(models.Model):
    id = models.BigAutoField(primary_key=True)
    cus_production_process_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    original_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    is_percent_up = models.IntegerField()
    show_from = models.DateTimeField(blank=True, null=True)
    show_to = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cus_production_setting'


class CustomerBanks(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_banks'


class CustomerContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=254, blank=True, null=True)
    fax = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_contacts'


class CustomerDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=254, blank=True, null=True)
    fax = models.CharField(max_length=254, blank=True, null=True)
    tax_number = models.CharField(max_length=254, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_detail'


class CustomerWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    credit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    debit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    reduce = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_wallets'


class CustomerWarehouses(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    ward = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_warehouses'


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DebitDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    invoice_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_origin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'debit_detail'


class DeleteMaterialDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_delete_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_quota_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delete_material_detail'


class Delivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class GoodsStockIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_storage_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    import_product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stock_in'


class GoodsStockOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    is_confirm = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    delivery_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stock_out'


class GoodsStockOutAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    pi_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    goods_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stock_out_assign'


class GoodsStockOutDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    product_storage_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_id = models.PositiveBigIntegerField(blank=True, null=True)
    goods_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    stock_quantity = models.DecimalField(max_digits=18, decimal_places=6)
    pi_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stock_out_detail'


class GoodsStockOutStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goods_stock_out_status'


class ImportProductStorageAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_product_storage_assign'


class ImportProductStorageDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    goods_stock_in_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_storage_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_pattern_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_product_storage_details'


class ImportProductStorageStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_product_storage_status'


class ImportProductStorages(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    is_confirm = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    delivery_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_product_storages'


class ImportPurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    delivery_name = models.CharField(max_length=254, blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    is_confirm = models.IntegerField()
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    is_auto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'import_purchase_order'


class ImportPurchaseOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_stock_in_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    assign_import_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_purchase_order_detail'


class ImportPurchaseOrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_purchase_order_status'


class ImportReturnProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    import_return_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    return_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6)
    price = models.DecimalField(max_digits=24, decimal_places=10)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    return_product_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'import_return_product_detail'


class ImportReturnProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    import_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_return_products'


class InvoiceDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    invoice_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_detail'


class InvoiceInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    invoice_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_info'


class Invoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class ManufactureDept(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_dept'


class ManufactureDeptDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    leaktime = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_dept_detail'


class ManufactureProd(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_prod'


class ManufactureProductExport(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    manufacture_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_import = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    receiver = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_product_export'


class ManufactureProductExportDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    manufacture_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    receiver = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_product_export_detail'


class ManufactureProductImport(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    manufacture_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_product_import'


class ManufactureProductImportDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    manufacture_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_product_import_detail'


class ManufactureProductWarehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_product_warehouse'


class ManufactureTaskDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    status_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_del_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_comp_id = models.PositiveBigIntegerField(blank=True, null=True)
    description_del = models.TextField(blank=True, null=True)
    min_prod_quan = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_prod_quan = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_task_detail'


class ManufactureTaskLink(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    parent_task_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_task_link'


class ManufactureTaskStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_task_status'


class ManufactureTasks(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacture_tasks'


class MaterialOffsetDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    material_offset_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    total_quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_offset_detail'


class MaterialOffsetPo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_offset_po'


class MaterialOffsetPoDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_offset_po_detail'


class MaterialOffsetPoStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_offset_po_status'


class MessageDepartments(models.Model):
    id = models.BigAutoField(primary_key=True)
    message_id = models.PositiveBigIntegerField(blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_departments'


class MessageUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    message_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)
    read = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_users'


class Messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=254, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    sender_id = models.PositiveBigIntegerField(blank=True, null=True)
    receiver_id = models.PositiveBigIntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


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
        managed = False
        db_table = 'order_booking'


class OrderBookingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    order_booking_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_booking_status'


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
        managed = False
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
        managed = False
        db_table = 'order_quota'


class OrderQuotaSuggest(models.Model):
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
    specification = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_quota_suggest'


class OrderShipped(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipped'


class OrderShippedDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_shipped_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_shipping_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipped_detail'


class OrderShipping(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipping'


class OrderShippingDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_shipping_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    ship_from = models.TextField(blank=True, null=True)
    ship_to = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    begin_ship_date = models.DateField(blank=True, null=True)
    end_ship_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipping_detail'


class OrderShippingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_shipping_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_shipping_status'


class OrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    set_complete_user_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_status'


class OrderWarehouse(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    packing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    total_shipping = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    total_shipped = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    remain = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_warehouse'


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
        managed = False
        db_table = 'orders'


class OutsourcingDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_child_code = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.IntegerField()
    qr_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    qrcode_stock_out = models.CharField(max_length=255, blank=True, null=True)
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    vnd_exchange = models.FloatField(blank=True, null=True)
    return_prod_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    import_return_prod_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    return_prod_stockout_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    import_return_prod_stockin_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_detail'


class OutsourcingDetailGraph(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    is_completed = models.IntegerField()
    outsourcing_child_code = models.CharField(max_length=254, blank=True, null=True)
    is_default = models.IntegerField()
    qr_code = models.CharField(max_length=254, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_detail_graph'


class OutsourcingInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    qrcode_stock_out = models.CharField(max_length=255, blank=True, null=True)
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    is_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_infos'


class OutsourcingOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    for_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'outsourcing_orders'


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


class OutsourcingQuota(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    loss_percentage = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    total_type = models.CharField(max_length=255, blank=True, null=True)
    total_quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    is_exported = models.IntegerField()
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    vnd_exchange = models.FloatField(blank=True, null=True)
    outsourcing_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)
    quota_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_quota'


class OutsourcingQuotaGraph(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_detail_graph_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    quota_percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    total_quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    is_exported = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    is_primary = models.IntegerField()
    parent_product_id = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    parent_index = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_quota_graph'


class OutsourcingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    set_complete_user_id = models.PositiveBigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outsourcing_status'


class PackingList(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    tracking_purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    vnd_exchange = models.FloatField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    stockin_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    return_prod_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    import_return_prod_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    return_prod_stockout_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    import_return_prod_stockin_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packing_list'


class PaymentMethods(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_methods'


class ProductColorDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_color_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_color_details'


class ProductColors(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_colors'


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
        managed = False
        db_table = 'product_detail'




class ProductInvoiceDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    pi_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    tax_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    total_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_invoice_details'


class ProductInvoiceInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    pi_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    shipment_date = models.DateField(blank=True, null=True)
    export_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    total_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    notify = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_invoice_infos'


class ProductInvoiceStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    pi_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_invoice_status'


class ProductInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_invoices'


class ProductMedias(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    re_order = models.PositiveBigIntegerField(blank=True, null=True)
    is_thumbnail = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_medias'


class ProductOrderHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_quota_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_detail_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    order_quota_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    pre_temp_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    temp_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_order_histories'


class ProductPatternDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    product_pattern_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pattern_detail'


class ProductPatternInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    rap_chop = models.CharField(max_length=254, blank=True, null=True)
    rap_ket = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_pattern_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pattern_info'


class ProductPatterns(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_patterns'


class ProductPeriodReports(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_period_reports'


class ProductQuantityTemporaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_order_history_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_stock_history_id = models.PositiveBigIntegerField(blank=True, null=True)
    temp_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    product_detail_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_quantity_temporaries'


class ProductRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    imp_real_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    star_num = models.PositiveBigIntegerField(blank=True, null=True)
    review = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_rating'


class ProductReportLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    period_report_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_report_locations'


class ProductSpecificationDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_specification_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_specification_details'


class ProductSpecifications(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_specifications'


class ProductStages(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    period_report_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stages'


class ProductStockHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    pre_product_detail_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    product_detail_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    stock_in_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    stock_out_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    pre_temp_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    temp_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    import_po_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_histories'


class ProductStockIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    uniqid = models.CharField(max_length=254, blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    qrcode = models.CharField(max_length=255)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    default_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    unit_exchange_rate = models.FloatField(blank=True, null=True)
    unit_exchange = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_in'


class ProductStockInCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    import_product_storage_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_in_certificates'


class ProductStockInRealDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    quantity_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    product_stock_in_real_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    import_return_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    req_stockin_product_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_in_real_details'


class ProductStockInReals(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_auto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_stock_in_reals'


class ProductStockOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_confirm = models.IntegerField()
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    delivery_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_out'


class ProductStockOutCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    goods_stock_out_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_out_certificates'


class ProductStockOutStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_out_status'


class ProductStockStageHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    previous_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    wh_correction_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_stage_histories'


class ProductStockStages(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock_stages'


class ProductStocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stocks'


class ProductStorageInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    company_branch_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_storage_infos'


class ProductStorageLocationInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_storage_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_storage_location_infos'


class ProductStorageLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_storage_locations'


class ProductStorageStages(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_storage_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_storage_stages'


class ProductStorages(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_storages'


class ProductTypeDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_type_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_type_details'


class ProductTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_types'


class ProductUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    source_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    result_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    source_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    result_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_unit'


class ProductUnitExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    source_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    result_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    source_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    result_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_unit_exchange'


class ProductionDepartment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_department'


class ProductionDiary(models.Model):
    id = models.BigAutoField(primary_key=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    po = models.CharField(max_length=255, blank=True, null=True)
    complete_percent = models.DecimalField(max_digits=12, decimal_places=6, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_department_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_complete = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    diary_date = models.DateField(blank=True, null=True)
    team = models.CharField(max_length=255, blank=True, null=True)
    quantity_manufacture_prod = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    manufacture_prod_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_sync = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'production_diary'


class ProductionNotExistOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    buyer_name = models.CharField(max_length=255, blank=True, null=True)
    style_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_not_exist_order'


class ProductionOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    delivery_name = models.CharField(max_length=254, blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    is_exported = models.IntegerField()
    token = models.CharField(max_length=191, blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_order_detail'


class ProductionOrderInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    completed_at = models.DateField(blank=True, null=True)
    production_department_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_complete = models.IntegerField()
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_order_info'


class ProductionOrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    set_complete_user_id = models.PositiveBigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_order_status'


class ProductionOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_orders'


class ProductionStockOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    uniqid = models.CharField(max_length=254, blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    assign_product_stockout_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    production_order_detail_id = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    stock_quantity = models.DecimalField(max_digits=18, decimal_places=6)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    prod_secondary_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_stock_out'


class ProductionTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    prod_not_exist_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    target_quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    actual_quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    complete_percent = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_tracking'


class ProductionTrackingDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    production_tracking_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    prod_not_exist_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    working_time_id = models.PositiveBigIntegerField(blank=True, null=True)
    manufacture_dept_id = models.PositiveBigIntegerField(blank=True, null=True)
    target_quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_tracking_detail'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class PurchaseOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    tax_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    arrange_number = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    is_global = models.IntegerField()
    unique_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_tax_include = models.IntegerField()
    is_completed = models.IntegerField()
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    vnd_exchange = models.FloatField(blank=True, null=True)
    is_auto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchase_order_detail'


class PurchaseOrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    set_complete_user_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order_status'


class PurchaseOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_orders'


class ReduceDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    invoice_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reduce_detail'


class ReqChangeMaterialPo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_po'


class ReqChangeMaterialPoDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_po_detail'


class ReqChangeMaterialPoStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_po_status'


class ReqChangeMaterialProduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_production'


class ReqChangeMaterialProductionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_production_detail'


class ReqChangeMaterialProductionStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_material_production_status'


class ReqChangePricePo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_price_po'


class ReqChangePricePoDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_change_price_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_req_change_price_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    old_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    new_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    new_currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    old_currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    product_stock_in_real_detail_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_price_po_details'


class ReqChangePricePoStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    req_change_price_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_price_po_status'


class ReqChangeProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_change_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    code_new = models.CharField(max_length=255, blank=True, null=True)
    name_new = models.CharField(max_length=255, blank=True, null=True)
    short_code_new = models.CharField(max_length=255, blank=True, null=True)
    unit_id_new = models.PositiveBigIntegerField(blank=True, null=True)
    product_color_id_new = models.PositiveBigIntegerField(blank=True, null=True)
    product_type_id_new = models.PositiveBigIntegerField(blank=True, null=True)
    product_specification_id_new = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id_new = models.PositiveBigIntegerField(blank=True, null=True)
    is_outsourcing_new = models.PositiveBigIntegerField(blank=True, null=True)
    code_old = models.CharField(max_length=255, blank=True, null=True)
    name_old = models.CharField(max_length=255, blank=True, null=True)
    short_code_old = models.CharField(max_length=255, blank=True, null=True)
    unit_id_old = models.PositiveBigIntegerField(blank=True, null=True)
    product_color_id_old = models.PositiveBigIntegerField(blank=True, null=True)
    product_type_id_old = models.PositiveBigIntegerField(blank=True, null=True)
    product_specification_id_old = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id_old = models.PositiveBigIntegerField(blank=True, null=True)
    is_outsourcing_old = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    specification_new = models.CharField(max_length=255, blank=True, null=True)
    specification_old = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_product_detail'


class ReqChangeProductInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    req_change_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_product_info'


class ReqChangeProductMaterialProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_change_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    ratio = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_product_material_product'


class ReqDeleteMaterialPo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_po'


class ReqDeleteMaterialPoDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    packing_list_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_po_detail'


class ReqDeleteMaterialPoStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_po_status'


class ReqDeleteMaterialProduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_production'


class ReqDeleteMaterialProductionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    production_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_production_detail'


class ReqDeleteMaterialProductionStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_material_production_status'


class ReqDeletePo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_po'


class ReqDeletePoStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    delete_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_po_status'


class ReqDeleteProduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_production'


class ReqDeleteProductionStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_delete_production_status'


class ReqMaterialOffsetProduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_material_offset_production'


class ReqMaterialOffsetProductionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    production_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    specification = models.TextField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_exported = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_material_offset_production_detail'


class ReqMaterialOffsetProductionStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_material_offset_production_status'


class ReqMergeProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_merge_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    code_merge = models.CharField(max_length=255, blank=True, null=True)
    name_merge = models.CharField(max_length=255, blank=True, null=True)
    short_code_merge = models.CharField(max_length=255, blank=True, null=True)
    unit_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    product_color_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    product_type_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    product_specification_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id_merge = models.PositiveBigIntegerField(blank=True, null=True)
    is_outsourcing_merge = models.PositiveBigIntegerField(blank=True, null=True)
    specification_merge = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_merge_product_detail'


class ReqMergeProductInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    req_merge_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_merge_product_info'


class ReqStockinProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_stockin_product'


class ReqStockinProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_import = models.CharField(max_length=255, blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    set_complete_user_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_stockin_product_detail'


class ReqStockinProductInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_stockin_product_info'


class ReqStockinProductStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    set_complete_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_stockin_product_status'


class ReqStockoutProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_stockout_product'


class ReqStockoutProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    is_export = models.CharField(max_length=255, blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_exported = models.IntegerField()
    is_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'req_stockout_product_detail'


class ReqStockoutProductInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    department_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_stockout_product_info'


class ReqStockoutProductStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    set_complete_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_stockout_product_status'


class RequestAdjustImportOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_adjust_import_order'


class RequestAdjustImportOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_adjust_import_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_po_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    origin_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    adjust_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    is_increase = models.IntegerField()
    disparity_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_adjust_import_order_detail'


class RequestChangeMaterial(models.Model):
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
        managed = False
        db_table = 'request_change_material'


class RequestChangeMaterialStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_change_material_status'


class RequestDeleteMaterial(models.Model):
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
        managed = False
        db_table = 'request_delete_material'


class RequestDeleteMaterialStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_delete_material_status'


class RequestDeleteOrderBooking(models.Model):
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
        managed = False
        db_table = 'request_delete_order_booking'


class RequestDeleteOrderBookingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_delete_order_booking_status'


class RequestMaterialOffset(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    priority = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_material_offset'


class RequestMaterialOffsetStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    request_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_material_offset_status'


class ReturnProductDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    return_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6)
    price = models.DecimalField(max_digits=24, decimal_places=10)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    import_date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'return_product_detail'


class ReturnProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_import = models.IntegerField()
    is_outsourcing = models.IntegerField()
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    export_date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    qrcode = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_complete = models.IntegerField()
    user_set_complete = models.BigIntegerField(blank=True, null=True)
    is_exported = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'return_products'


class SemiProductInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    semi_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_infos'


class SemiProductOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    sp_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    semi_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    order_id = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.CharField(max_length=254, blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_order_detail'


class SemiProductOrderInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    sp_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    supplier_delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    payment_method_id = models.PositiveBigIntegerField(blank=True, null=True)
    delivery_at = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    qrcode_stock_out = models.CharField(max_length=255, blank=True, null=True)
    vnd_exchange_rate = models.FloatField(blank=True, null=True)
    is_complete = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_order_infos'


class SemiProductOrderQuota(models.Model):
    id = models.BigAutoField(primary_key=True)
    sp_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    sp_order_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    quota = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    specification = models.CharField(max_length=254, blank=True, null=True)
    is_exported = models.IntegerField()
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_order_quota'


class SemiProductOrderStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    sp_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_order_status'


class SemiProductOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_orders'


class SemiProductStorage(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_storage'


class SemiProductStorageDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    sp_storage_id = models.PositiveBigIntegerField(blank=True, null=True)
    semi_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_product_storage_detail'


class SemiProducts(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semi_products'


class ShippingStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    english_name = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_status'


class StockInCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    import_po_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_in_certificates'


class StockOutCertificates(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    product_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_out_certificates'


class StockOutExcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_stock_out_id = models.PositiveBigIntegerField(blank=True, null=True)
    production_order_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    total_exported = models.DecimalField(max_digits=24, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_out_excess'


class SupplierBank(models.Model):
    id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_bank'


class SupplierContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=254, blank=True, null=True)
    fax = models.CharField(max_length=254, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_contact'


class SupplierCreditDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    supplier_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_supplier_credit_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_credit_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_credit_details'


class SupplierCreditStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    supplier_credit_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_credit_status'


class SupplierCredits(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_credits'


class SupplierDebitDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_debit_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_supplier_debit_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    total_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    supplier_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_stock_in_real_detail_id = models.CharField(max_length=255, blank=True, null=True)
    req_change_price_po_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_debit_details'


class SupplierDebitStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    supplier_debit_detail_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_debit_status'


class SupplierDebits(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    product_stock_real_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_debits'


class SupplierDelivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    delivery_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_delivery'


class SupplierInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=254, blank=True, null=True)
    fax = models.CharField(max_length=254, blank=True, null=True)
    tax_number = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_outsourcing = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplier_info'


class SupplierReduceDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_reduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_supplier_reduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    supplier_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_reduce_details'


class SupplierReduceStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=254, blank=True, null=True)
    supplier_reduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_reduce_status'


class SupplierReduces(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_reduces'


class SupplierWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    debit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    reduce = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_wallets'


class SupplierWarehouses(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    ward = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    city = models.CharField(max_length=254, blank=True, null=True)
    zip_code = models.CharField(max_length=254, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier_warehouses'


class Suppliers(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class TaskStatusChangeHis(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    task_id = models.PositiveBigIntegerField(blank=True, null=True)
    status_id = models.PositiveBigIntegerField(blank=True, null=True)
    old_status_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task_status_change_his'


class Tax(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class TrackingOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    tracking_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_order'


class TrackingOrderDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    tracking_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    percent = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_order_detail'


class TrackingPurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    tracking_purchase_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracking_purchase_order'


class Units(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class WalletStages(models.Model):
    id = models.BigAutoField(primary_key=True)
    credit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    debit = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    reduce = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    customer_wallet_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallet_stages'


class WarehouseContainer(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_container'


class WarehouseContainerInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse_container_id = models.PositiveBigIntegerField(blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_sector_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_source = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_container_info'


class WarehouseInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    media_source = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    company_branch_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_infos'


class WarehouseLocationInfos(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse_location_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_container_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_sector_id = models.PositiveBigIntegerField(blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=254, blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    qrcode = models.CharField(max_length=254, blank=True, null=True)
    lat = models.CharField(max_length=254, blank=True, null=True)
    lng = models.CharField(max_length=254, blank=True, null=True)
    media_source = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_location_infos'


class WarehouseLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_locations'


class WarehouseSector(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_sector'


class WarehouseSectorInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    warehouse_sector_id = models.PositiveBigIntegerField(blank=True, null=True)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)
    warehouse_id = models.PositiveBigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_id = models.PositiveBigIntegerField(blank=True, null=True)
    media_source = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_sector_info'


class Warehouses(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouses'


class WhCorrectionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    wh_correction_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    currency_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_increase = models.IntegerField()
    quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    stock_quantity_before = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    stock_quantity_after = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_correction_detail'


class WhCorrections(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    prod_period_report_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wh_corrections'


class WorkingTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'working_time'
