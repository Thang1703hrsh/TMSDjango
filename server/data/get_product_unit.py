# from .models import *
# import pandas as pd

# # def dfProductUnit():
# dfProductUnit = ProductDetail.objects.raw("""  
#         SELECT 1 id, PU.product_id , PU.id AS product_unit_id, PU.unit_id, PU.is_default
#         FROM product_unit AS PU JOIN product_detail AS PD 
#                 ON PD.product_id = PU.product_id
#         WHERE PU.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL 
            
#         """)
# dfProductUnit = pd.DataFrame([item.__dict__ for item in dfProductUnit]).drop(['_state', 'id'], axis=1)
# print(dfProductUnit)
# dfProductUnit.to_csv('../data_csv/ProductUnit.csv', index= False)

# # def dfProductUnit():
# dfProductUnitExchange = ProductDetail.objects.raw("""  
#         SELECT 1 id, PUE.product_id, PUE.source_unit_id, PUE.result_unit_id, PUE.source_quantity, PUE.result_quantity
#         FROM product_unit_exchange AS PUE JOIN product_detail AS PD 
#                 ON PD.product_id = PUE.product_id 
            
#         WHERE PUE.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL 
            
#         """)
# dfProductUnitExchange = pd.DataFrame([item.__dict__ for item in dfProductUnitExchange]).drop(['_state', 'id'], axis=1)
# print(dfProductUnitExchange)
# dfProductUnitExchange.to_csv('../data_csv/ProductUnitExchange.csv', index= False)

