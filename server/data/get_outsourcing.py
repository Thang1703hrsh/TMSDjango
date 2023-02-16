# from .models import *
# import pandas as pd


# ## Outsourcing Stock In Detail
# dfOutsourcingStockIn = ProductDetail.objects.raw("""  
#         SELECT 1 id, OD.outsourcing_order_id ,OD.product_id AS outsourcing_product_id, OD.is_complete AS is_complete_detail ,OD.quantity AS outsourcing_quantity ,PSIRD.quantity AS quantity_stock_in
#                 FROM outsourcing_detail OD JOIN outsourcing_orders OO 
#                                 ON OO.id = OD.outsourcing_order_id
#                         LEFT JOIN product_stock_in_real_details AS PSIRD 
#                                 ON OD.outsourcing_order_id = PSIRD.outsourcing_order_id AND OD.product_id = PSIRD.product_id
#                 WHERE OD.deleted_at IS NULL  
#                         AND OO.deleted_at IS NULL  
#                         AND PSIRD.deleted_at IS NULL  
#                 ORDER BY `OD`.`outsourcing_order_id` DESC;
#         """)

# dfOutsourcingStockIn = pd.DataFrame([item.__dict__ for item in dfOutsourcingStockIn]).drop(['_state', 'id'], axis=1)
# print(dfOutsourcingStockIn)
# dfOutsourcingStockIn.to_csv('data_csv/OutsourcingStockIn.csv', index= False)


# ## Outsourcing Detail
# dfOutSourcingDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, OI.outsourcing_order_id , OI.name, OI.is_complete AS is_complete_order , OD.product_id ,OD.quantity AS outsourcing_quantity , OD.is_complete AS is_complete_order_detail, OS.status AS outsourcing_status
#                 FROM outsourcing_infos OI LEFT JOIN outsourcing_detail OD
#                         ON OI.outsourcing_order_id = OD.outsourcing_order_id
#                                 JOIN outsourcing_orders OO 
#                         ON OO.id = OD.outsourcing_order_id
#                                 JOIN outsourcing_status AS OS
#                         ON OS.outsourcing_order_id = OI.outsourcing_order_id

#                 WHERE OD.deleted_at IS NULL  
#                     AND OI.deleted_at IS NULL  
#                     AND OO.deleted_at IS NULL  
#                     AND OS.deleted_at IS NULL 
                        
#                 ORDER BY `OD`.`outsourcing_order_id` DESC;
#         """)

# dfOutSourcingDetail = pd.DataFrame([item.__dict__ for item in dfOutSourcingDetail]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingDetail)
# dfOutSourcingDetail.to_csv('data_csv/OutSourcingDetail.csv', index= False)


# ## dfOutSourcing Material
# dfOutSourcingMaterial = ProductDetail.objects.raw(""" 
#         SELECT 1 id, OQ.outsourcing_detail_id, OD.product_id AS outsourcing_product_id , OD.outsourcing_order_id, OD.quantity AS quantity_outsourcing_detail, OD.is_complete AS is_complete_detail , OQ.product_id , OQ.total_quota, OQ.is_exported ,OQ.quota_percent  
#                 FROM outsourcing_orders OO LEFT JOIN outsourcing_quota AS OQ 
#                                 ON OO.id = OQ.outsourcing_order_id
#                         LEFT JOIN outsourcing_detail AS OD 
#                                 ON OQ.outsourcing_detail_id = OD.id AND OQ.outsourcing_order_id = OD.outsourcing_order_id
                
#                 WHERE OD.deleted_at IS NULL  
#                         AND OQ.deleted_at IS NULL  
#                         AND OO.deleted_at IS NULL  
                        
#                 ORDER BY `OD`.`outsourcing_order_id` ASC;
#         """)

# dfOutSourcingMaterial = pd.DataFrame([item.__dict__ for item in dfOutSourcingMaterial]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingMaterial)
# dfOutSourcingMaterial.to_csv('data_csv/OutSourcingMaterial.csv', index= False)


# ## OutSourcing StockOut
# dfOutSourcingStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.product_id, OQ.outsourcing_order_id , OQ.total_quota AS quantity_stock_out, OQ.is_exported, OQ.outsourcing_detail_id, OQ.outsourcing_detail_id ,PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_outsourcing
#                 FROM outsourcing_quota AS OQ 
#                         JOIN outsourcing_orders OO 
#                                 ON OO.id = OQ.outsourcing_order_id
#                         LEFT JOIN assign_product_stockout AS APS
#                                 ON OQ.outsourcing_order_id = APS.outsourcing_order_id AND APS.outsourcing_quota_id = OQ.id 
#                         LEFT JOIN production_stock_out AS PSO
#                                 ON PSO.product_id = OQ.product_id AND PSO.assign_product_stockout_id = APS.id
                            
#                 WHERE OQ.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                         AND OO.deleted_at IS NULL
#                 ORDER BY OQ.product_id ASC;
#         """)
# dfOutSourcingStockOut = pd.DataFrame([item.__dict__ for item in dfOutSourcingStockOut]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingStockOut)
# dfOutSourcingStockOut.to_csv('data_csv/OutSourcingStockOut.csv', index= False)



# ## Outsourcing 
# dfOutSourcingOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, OI.outsourcing_order_id , OI.name, OI.is_complete AS is_complete_infos, OS.status
#                 FROM outsourcing_infos OI JOIN outsourcing_orders OO 
#                         ON OO.id = OI.outsourcing_order_id
#                         JOIN outsourcing_status OS
#                         ON OS.outsourcing_order_id = OO.id
#                 WHERE OI.deleted_at IS NULL  
#                     AND OO.deleted_at IS NULL  
#                     AND OS.deleted_at IS NULL  
                        
#                 ORDER BY OI.outsourcing_order_id ASC;
#         """)

# dfOutSourcingOrder = pd.DataFrame([item.__dict__ for item in dfOutSourcingOrder]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingOrder)
# dfOutSourcingOrder.to_csv('data_csv/OutSourcingOrder.csv', index= False)




# # # Import Outsourcing Stock In 
# # dfImportOutSourcing = ProductDetail.objects.raw("""  
# #         SELECT 1 id, AIS.outsourcing_order_id , IPOD.assign_import_order_id, IPOD.product_id, IPOD.product_unit_id, IPOD.quantity
# #                 FROM assign_import_order AIS LEFT JOIN import_purchase_order_detail IPOD 
# #                         ON AIS.id = IPOD.assign_import_order_id
# #                 WHERE AIS.deleted_at IS NULL  
# #                     AND IPOD.deleted_at IS NULL  
# #                     AND AIS.outsourcing_order_id IS NOT NULL  
                        
# #                 ORDER BY `AIS`.`outsourcing_order_id` ASC;
# #         """)

# # dfImportOutSourcing = pd.DataFrame([item.__dict__ for item in dfImportOutSourcing]).drop(['_state', 'id'], axis=1)
# # print(dfImportOutSourcing)
# # dfImportOutSourcing.to_csv('data_csv/ImportOutSourcing.csv', index= False)


