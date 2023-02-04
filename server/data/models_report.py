# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AssignIntroduceDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    introduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    introduce_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    step = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_introduce_details'


class AssignMaterialOutsoucing(models.Model):
    id = models.BigAutoField(primary_key=True)
    outsourcing_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    outsourcing_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    outsourcing_percent = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    product_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_calculated = models.IntegerField()
    outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assign_material_outsoucing'


class CheckMaterialReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=254, blank=True, null=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    total_record = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_material_report'


class CheckMaterialReportDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_id = models.PositiveBigIntegerField(blank=True, null=True)
    material = models.CharField(max_length=254, blank=True, null=True)
    db_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    db_temporary_deduction = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    db_imported = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    db_exported = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    db_begin_quan_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    db_final_quan_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    file_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    file_temporary_deduction = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    file_imported = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    flie_exported = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    file_begin_quan_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    file_final_quan_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'check_material_report_detail'


class IntroUserTrackings(models.Model):
    id = models.BigAutoField(primary_key=True)
    introduce_id = models.PositiveBigIntegerField(blank=True, null=True)
    assign_introduce_detail_id = models.PositiveBigIntegerField(blank=True, null=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    is_skip = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intro_user_trackings'


class IntroduceDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'introduce_details'


class Introduces(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'introduces'


class MarkedReportHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    begin_need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    begin_need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marked_report_history'


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


class MaterialReports(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_for_outsourcing = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    is_calculated = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    outsourcing_stock_out = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    temporary_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'material_reports'


class OrderTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    old_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_tracking'


class ProductExistingReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    total_record = models.BigIntegerField(blank=True, null=True)
    current_record = models.BigIntegerField(blank=True, null=True)
    percent = models.BigIntegerField(blank=True, null=True)
    is_report_product = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_existing_report'


class ReportPrimaryProductNeeds(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    quantity_for_secondary = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_primary_product_needs'


class ReportProductNeedHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    report_product_need_id = models.PositiveBigIntegerField(blank=True, null=True)
    old_need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_product_need_history'


class ReportProductNeedPrimaryHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    report_primary_product_need_id = models.PositiveBigIntegerField(blank=True, null=True)
    creator_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    quantity_for_secondary = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_ordered_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_need_order_quantity = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_in_stock = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    old_quantity_for_secondary = models.DecimalField(max_digits=24, decimal_places=10, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_product_need_primary_history'


class ReportProductNeeds(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_id = models.PositiveBigIntegerField(blank=True, null=True)
    product_unit_id = models.PositiveBigIntegerField(blank=True, null=True)
    need_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    ordered_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    need_order_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    in_stock = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_product_needs'


class ReqChangeProductHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_change_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    column_name = models.CharField(max_length=255, blank=True, null=True)
    content_new = models.CharField(max_length=255, blank=True, null=True)
    content_old = models.CharField(max_length=255, blank=True, null=True)
    row_change_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_change_product_history'


class ReqMergeProductHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    req_merge_product_id = models.PositiveBigIntegerField(blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    column_name = models.CharField(max_length=255, blank=True, null=True)
    content_new = models.CharField(max_length=255, blank=True, null=True)
    content_old = models.CharField(max_length=255, blank=True, null=True)
    row_change_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_merge_product_history'


class RequestAdjustImportOrderHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_adjust_import_order_id = models.PositiveBigIntegerField(blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    record_id_change = models.PositiveBigIntegerField(blank=True, null=True)
    record_column_change = models.CharField(max_length=255, blank=True, null=True)
    old_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request_adjust_import_order_history'
