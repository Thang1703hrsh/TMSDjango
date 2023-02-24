from .models_data import *
import pandas as pd

dfManufactureProdExport = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_product_export MPE
        WHERE MPE.deleted_at IS NULL
        """)

dfManufactureProdExport = pd.DataFrame([item.__dict__ for item in dfManufactureProdExport]).drop(['_state', 'id'], axis=1)
print(dfManufactureProdExport)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)


dfManufactureProdExportDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_product_export_detail MPED
        WHERE MPED.deleted_at IS NULL
        """)

dfManufactureProdExportDetail = pd.DataFrame([item.__dict__ for item in dfManufactureProdExportDetail]).drop(['_state', 'id'], axis=1)
print(dfManufactureProdExportDetail)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)


