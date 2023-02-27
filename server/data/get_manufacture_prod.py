from .models_data import *
import pandas as pd

dfManufactureProd = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_prod MP
        WHERE MP.deleted_at IS NULL
        """)

dfManufactureProd = pd.DataFrame([item.__dict__ for item in dfManufactureProd]).drop(['_state'], axis=1)
print(dfManufactureProd)
dfManufactureProd.to_csv('../data_csv/ManufactureProd.csv', index= False)
