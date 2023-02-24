from .models_data import *
import pandas as pd

dfManufactureProdImport = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_product_import MPI
        WHERE MPI.deleted_at IS NULL
        """)

dfManufactureProdImport = pd.DataFrame([item.__dict__ for item in dfManufactureProdImport]).drop(['_state', 'id'], axis=1)
print(dfManufactureProdImport)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)


dfManufactureProdImportDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_product_import_detail MPID
        WHERE MPID.deleted_at IS NULL
        """)

dfManufactureProdImportDetail = pd.DataFrame([item.__dict__ for item in dfManufactureProdImportDetail]).drop(['_state', 'id'], axis=1)
print(dfManufactureProdImportDetail)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)

dfManufactureProdWarehouse = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_product_warehouse MPW
        WHERE MPW.deleted_at IS NULL
        """)

dfManufactureProdWarehouse = pd.DataFrame([item.__dict__ for item in dfManufactureProdWarehouse]).drop(['_state', 'id'], axis=1)
print(dfManufactureProdWarehouse)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)



