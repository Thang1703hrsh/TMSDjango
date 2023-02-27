from .models_data import *
import pandas as pd

## Outsourcing Stock In Detail
dfManufactureDept = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_dept MD
        WHERE MD.deleted_at IS NULL
        """)

dfManufactureDept = pd.DataFrame([item.__dict__ for item in dfManufactureDept]).drop(['_state', 'id'], axis=1)
print(dfManufactureDept)
dfManufactureDept.to_csv('../data_csv/ManufactureDept.csv', index= False)

dfManufactureDeptDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_dept_detail MDD
        WHERE MDD.deleted_at IS NULL
        """)

dfManufactureDeptDetail = pd.DataFrame([item.__dict__ for item in dfManufactureDeptDetail]).drop(['_state', 'id'], axis=1)
print(dfManufactureDeptDetail)
dfManufactureDeptDetail.to_csv('../data_csv/ManufactureDeptDetail.csv', index= False)


