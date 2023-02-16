# from .models import *
# import pandas as pd



# ## dfOutSourcingMaterial
# dfOutSourcingMaterial = ProductDetail.objects.raw(""" 
#         SELECT 1 id, OQ.outsourcing_detail_id, OD.product_id AS outsourcing_product_id , OD.outsourcing_order_id, OD.quantity AS quantity_outsourcing_detail, OQ.product_id , OQ.total_quota, OQ.is_exported ,OQ.quota_percent 
#                 FROM outsourcing_detail AS OD RIGHT JOIN outsourcing_quota AS OQ 
#                                 ON OQ.outsourcing_detail_id = OD.id AND OQ.outsourcing_order_id = OD.outsourcing_order_id
#                 WHERE OD.deleted_at IS NULL  
#                         AND OQ.deleted_at IS NULL  
                        
#                 ORDER BY `OD`.`outsourcing_order_id` ASC;
#         """)

# dfOutSourcingMaterial = pd.DataFrame([item.__dict__ for item in dfOutSourcingMaterial]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingMaterial)
# dfOutSourcingMaterial.to_csv('data_csv/OutSourcingMaterial.csv', index= False)
