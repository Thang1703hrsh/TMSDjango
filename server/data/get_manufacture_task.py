from .models_data import *
import pandas as pd

dfManufactureTask = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_tasks MT
        WHERE MT.deleted_at IS NULL
        """)

dfManufactureTask = pd.DataFrame([item.__dict__ for item in dfManufactureTask]).drop(['_state', 'id'], axis=1)
print(dfManufactureTask)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)


dfManufactureTaskStatus = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_task_status MTS
        WHERE MTS.deleted_at IS NULL
        """)

dfManufactureTaskStatus = pd.DataFrame([item.__dict__ for item in dfManufactureTaskStatus]).drop(['_state', 'id'], axis=1)
print(dfManufactureTaskStatus)
# dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)



dfManufactureTaskDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_task_detail MTD
        WHERE MTD.deleted_at IS NULL
        """)

dfManufactureTaskDetail = pd.DataFrame([item.__dict__ for item in dfManufactureTaskDetail]).drop(['_state', 'id'], axis=1)
print(dfManufactureTaskDetail)



dfManufactureTaskLink = ProductDetail.objects.raw("""  
        SELECT *
        FROM manufacture_task_link MTL
        WHERE MTL.deleted_at IS NULL
        """)

dfManufactureTaskLink = pd.DataFrame([item.__dict__ for item in dfManufactureTaskLink]).drop(['_state', 'id'], axis=1)
print(dfManufactureTaskLink)


