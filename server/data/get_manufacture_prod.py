from .models_data import *
import pandas as pd

dfManufactureProd = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_prod MP
        WHERE MP.deleted_at IS NULL
        """)

dfManufactureProd = pd.DataFrame([item.__dict__ for item in dfManufactureProd]).drop(['_state', 'id'], axis=1)
print(dfManufactureProd)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)
