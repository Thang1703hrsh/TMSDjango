# from .models_data import *
# import pandas as pd

# ## Outsourcing Stock In Detail
# dfManufactureDept = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM manufacture_dept MD
#         WHERE MD.deleted_at IS NULL
#         """)

# dfManufactureDept = pd.DataFrame([item.__dict__ for item in dfManufactureDept]).drop(['_state', 'id'], axis=1)
# print(dfManufactureDept)
# # dfManufacture.to_csv('data_csv/MaterialReports.csv', index= False)

# dfManufactureDeptDetail = ProductDetail.objects.raw("""  
#         SELECT MDD.code , MDD.name, MDD.creator_id (CAST(RSP.updated_at AS DATE)) AS time_create, MDD.manufacture_dept_id , MDD.department_id
#         FROM manufacture_dept_detail MDD
#         WHERE MDD.deleted_at IS NULL
#         """)

# dfManufactureDeptDetail = pd.DataFrame([item.__dict__ for item in dfManufactureDeptDetail]).drop(['_state', 'id'], axis=1)
# print(dfManufactureDeptDetail)


