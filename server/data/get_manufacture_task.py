# from .models_data import *
# import pandas as pd

# dfManufactureTask = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM manufacture_tasks MT
#         WHERE MT.deleted_at IS NULL
#         """)

# dfManufactureTask = pd.DataFrame([item.__dict__ for item in dfManufactureTask]).drop(['_state', 'id'], axis=1)
# print(dfManufactureTask)
# dfManufactureTask.to_csv('../data_csv/ManufactureTask.csv', index= False)


# dfManufactureTaskStatus = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM manufacture_task_status MTS
#         WHERE MTS.deleted_at IS NULL
#         """)

# dfManufactureTaskStatus = pd.DataFrame([item.__dict__ for item in dfManufactureTaskStatus]).drop(['_state', 'id'], axis=1)
# print(dfManufactureTaskStatus)
# dfManufactureTaskStatus.to_csv('../data_csv/ManufactureTaskStatus.csv', index= False)



# dfManufactureTaskDetail = ProductDetail.objects.raw("""  
#         SELECT MTD.* , MTS.code AS code_status, MTS.name AS name_status
#         FROM manufacture_task_detail MTD LEFT JOIN manufacture_task_status MTS ON MTD.status_id = MTS.id
#         """)

# dfManufactureTaskDetail = pd.DataFrame([item.__dict__ for item in dfManufactureTaskDetail]).drop(['_state', 'id'], axis=1)
# print(dfManufactureTaskDetail)
# dfManufactureTaskDetail.to_csv('../data_csv/ManufactureTaskDetail.csv', index= False)



# dfManufactureTaskLink = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM manufacture_task_link MTL
#         WHERE MTL.deleted_at IS NULL
#         """)

# dfManufactureTaskLink = pd.DataFrame([item.__dict__ for item in dfManufactureTaskLink]).drop(['_state', 'id'], axis=1)
# print(dfManufactureTaskLink)
# dfManufactureTaskLink.to_csv('../data_csv/ManufactureTaskLink.csv', index= False)


