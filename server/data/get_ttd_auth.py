
# from .models import *
# import pandas as pd

# dfUsers= ProductDetail.objects.raw("""  
#         SELECT 1 id, users.id as creator_id, users.fullname
#                 FROM ttd_auth.users AS users
#                 WHERE users.deleted_at IS NULL
                
#         """)

# dfUsers = pd.DataFrame([item.__dict__ for item in dfUsers]).drop(['_state', 'id'], axis=1)
# print(dfUsers)
# dfUsers.to_csv('../data_csv/Users.csv', index= False)

# dfSupplierDeliveryInfo= ProductDetail.objects.raw("""  
#         SELECT 1 id, SD.id as supplier_delivery_id, SD.supplier_id, SI.code as supplier_code,  SI.name as supplier_name
#                 FROM supplier_delivery AS SD LEFT JOIN supplier_info AS SI ON SD.supplier_id = SI.supplier_id
#                 WHERE SD.deleted_at IS NULL
#                     AND SI.deleted_at IS NULL
#         """)

# dfSupplierDeliveryInfo = pd.DataFrame([item.__dict__ for item in dfSupplierDeliveryInfo]).drop(['_state', 'id'], axis=1)
# print(dfSupplierDeliveryInfo)
# dfSupplierDeliveryInfo.to_csv('../data_csv/SupplierDeliveryInfo.csv', index= False)



