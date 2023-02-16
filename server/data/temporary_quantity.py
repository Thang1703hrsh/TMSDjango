# from .models_data import *
# import pandas as pd


# # req material offset production detail + Assign product stock + production_stock_out
# dfReqMaterialOffsetProduction = ProductDetail.objects.raw("""  
#         SELECT 1 id, RMOPD.product_id, RMOPD.order_id, RMOPD.request_id , RMOPD.quantity AS quantity_req_material_offset_production, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_req_material_offset_production
#                 FROM req_material_offset_production_detail AS RMOPD 
#                         LEFT JOIN assign_product_stockout AS APS
#                             ON RMOPD.request_id = APS.mat_offset_production_id AND APS.mat_offset_production_detail_id = RMOPD.id
                            
#                         LEFT JOIN production_stock_out AS PSO
#                                         ON PSO.product_id = RMOPD.product_id AND PSO.assign_product_stockout_id = APS.id
                            
#                 WHERE RMOPD.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                 ORDER BY RMOPD.product_id ASC;
#         """)
# dfReqMaterialOffsetProduction = pd.DataFrame([item.__dict__ for item in dfReqMaterialOffsetProduction]).drop(['_state', 'id'], axis=1)
# print(dfReqMaterialOffsetProduction)
# dfReqMaterialOffsetProduction.to_csv('data_csv/ReqMaterialOffsetProduction.csv', index= False)


# # Req stockout product detail + Assign product stock + production_stock_out
# dfReqStockoutProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id,RSPD.request_id, RSPD.quantity AS quantity_req_stockout, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_req_stockout
#                 FROM req_stockout_product_detail RSPD 
                
#                         LEFT JOIN assign_product_stockout APS
#                                 ON RSPD.request_id = APS.req_stockout_prod_id AND RSPD.id = APS.req_stockout_prod_detail_id
                                
#                         LEFT JOIN production_stock_out PSO
#                                 ON PSO.product_id = RSPD.product_id AND PSO.assign_product_stockout_id = APS.id 
 
#                 WHERE RSPD.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                 ORDER BY RSPD.product_id ASC;

#         """)

# dfReqStockoutProduct = pd.DataFrame([item.__dict__ for item in dfReqStockoutProduct]).drop(['_state', 'id'], axis=1)
# print(dfReqStockoutProduct)
# dfReqStockoutProduct.to_csv('data_csv/ReqStockoutProduct.csv', index= False)



# dfWhCorrectionDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, WHD.product_id, WHD.is_increase, WHD.quantity
#                 FROM product_detail AS PD JOIN wh_correction_detail AS WHD 
#                                 ON PD.product_id = WHD.product_id

#                 WHERE PD.deleted_at IS NULL
#                         AND WHD.deleted_at IS NULL
#                 ORDER BY PD.product_id ASC
#         """)

# dfWhCorrectionDetail = pd.DataFrame([item.__dict__ for item in dfWhCorrectionDetail]).drop(['_state', 'id'], axis=1)
# print(dfWhCorrectionDetail)
# dfWhCorrectionDetail.to_csv('data_csv/WhCorrectionDetail.csv', index= False)


# # Request stock out product detail
# dfReqStockoutProductDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id,RSPD.request_id, RSPD.quantity AS quantity_req_stockout, PSO.assign_product_stockout_id, PSO.quantity AS exported_req_quantity 
#                 FROM req_stockout_product_detail RSPD 
#                         LEFT JOIN production_stock_out PSO
#                                 ON PSO.product_id = RSPD.product_id
#                         LEFT JOIN assign_product_stockout APS
#                                 ON PSO.assign_product_stockout_id = APS.id AND RSPD.request_id = APS.req_stockout_prod_id

#                 WHERE RSPD.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                         AND APS.req_stockout_prod_id IS NOT NULL  
#                 ORDER BY `RSPD`.`product_id` ASC;

#         """)

# dfReqStockoutProductDetail = pd.DataFrame([item.__dict__ for item in dfReqStockoutProductDetail]).drop(['_state', 'id'], axis=1)
# print(dfReqStockoutProductDetail)
# dfReqStockoutProductDetail.to_csv('data_csv/ReqStockoutProductDetail.csv', index= False)



# ## Outsourcing Detail
# dfOutSourcingDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, OD.product_id, SUM(OD.quantity) AS outsourcing_quantity, SUM(quantity_stock_in) AS quantity_stock_in
#                 FROM outsourcing_detail OD LEFT JOIN (SELECT PSIRD.product_id, PSIRD.outsourcing_order_id, SUM(PSIRD.quantity) AS quantity_stock_in
#                                                 FROM product_stock_in_real_details AS PSIRD 
#                                                 WHERE PSIRD.deleted_at IS NULL  
#                                                 GROUP BY PSIRD.product_id, PSIRD.outsourcing_order_id) AS PSIRD
#                                         ON OD.outsourcing_order_id = PSIRD.outsourcing_order_id AND OD.product_id = PSIRD.product_id
#                 WHERE OD.deleted_at IS NULL  
                        
#                 GROUP BY OD.product_id 
#                 ORDER BY `OD`.`product_id` DESC;
#         """)

# dfOutSourcingDetail = pd.DataFrame([item.__dict__ for item in dfOutSourcingDetail]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingDetail)
# dfOutSourcingDetail.to_csv('data_csv/OutSourcingDetail.csv', index= False)





# # def readdfChild():
# dfRelationship = ProductDetail.objects.raw("""  
#         SELECT 1 id, OPM.outsourcing_product_id, OPM.product_id , PD.code as product_code , OPM.quantity as quota_outsourcing
#         FROM outsourcing_product_materials AS OPM JOIN product_detail AS PD 
#                                         ON OPM.product_id = PD.product_id 
#         WHERE OPM.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL 
        
#         """)

# dfRelationship = pd.DataFrame([item.__dict__ for item in dfRelationship]).drop(['_state', 'id'], axis=1)
# print(dfRelationship)
# dfRelationship.to_csv('data_csv/Relationship.csv', index= False)



# dfProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id , PD.code as product_code , PD.quantity AS quantity_product , PD.is_outsourcing
#         FROM product_detail PD 
#         WHERE PD.deleted_at IS NULL 
#                 AND PD.in_trash != 1
#         ORDER BY PD.product_id ASC
#         """)
# dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)
# print(dfProduct)
# dfProduct.to_csv('data_csv/Product.csv', index= False)


# dfOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.order_id, OQ.product_id, PD.code AS product_code, OQ.position ,OQ.total_quota
#                 FROM order_quota AS OQ JOIN product_detail PD 
#                         ON OQ.product_id = PD.product_id

#                 WHERE OQ.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
  
#                 ORDER BY OQ.order_id ASC;
#         """)
# dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)
# print(dfOrder)
# dfOrder.to_csv('data_csv/Order.csv', index= False)


# # Production order detail + Assign product stock + production_stock_out
# dfProductionOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, POD.product_id, POD.order_id, POD.production_order_id ,POD.quantity AS quantity_production_order, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_production_order
#                 FROM production_order_detail AS POD 
                        
#                         LEFT JOIN assign_product_stockout AS APS
#                                 ON POD.production_order_id = APS.production_order_id AND APS.production_order_detail_id = POD.id
                                
#                         LEFT JOIN production_stock_out AS PSO
#                                 ON PSO.product_id = POD.product_id AND PSO.assign_product_stockout_id = APS.id 
                            
#                 WHERE POD.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                 ORDER BY POD.product_id ASC;
#         """)
# dfProductionOrder = pd.DataFrame([item.__dict__ for item in dfProductionOrder]).drop(['_state', 'id'], axis=1)
# print(dfProductionOrder)
# dfProductionOrder.to_csv('data_csv/ProductionOrderDetail.csv', index= False)



# dfReturnProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RPD.product_id, RPD.return_product_id, RPD.quantity AS quantity_return_product, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_return_product
#                 FROM return_product_detail AS RPD 
#                         LEFT JOIN assign_product_stockout APS 
#                                 ON RPD.return_product_id = APS.return_product_id AND RPD.id = APS.return_product_detail_id
                                
#                         LEFT JOIN production_stock_out AS PSO
#                                 ON PSO.product_id = RPD.product_id AND APS.id = PSO.assign_product_stockout_id 

#                 WHERE PSO.deleted_at IS NULL
#                         AND RPD.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                 ORDER BY RPD.product_id ASC
#         """)

# dfReturnProduct = pd.DataFrame([item.__dict__ for item in dfReturnProduct]).drop(['_state', 'id'], axis=1)
# print(dfReturnProduct)
# dfReturnProduct.to_csv('data_csv/ReturnProduct.csv', index= False)


# dfOutSourcingQuota= ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, SUM(OQ.total_quota) AS total_quota
#                 FROM outsourcing_quota AS OQ JOIN product_detail AS PD 
#                                 ON PD.product_id = OQ.product_id
                                
#                 WHERE PD.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
#                 GROUP BY PD.product_id
#                 ORDER BY PD.product_id ASC
#         """)

# dfOutSourcingQuota = pd.DataFrame([item.__dict__ for item in dfOutSourcingQuota]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingQuota)
# dfOutSourcingQuota.to_csv('data_csv/OutSourcingQuota.csv', index= False)



# # Request stockin product status
# dfReqStockInProductStatus= ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id, RSPD.request_id, RSPD.quantity AS quantity_req_stockin, PSIRD.quantity AS quantity_in_stock_by_req
#                 FROM req_stockin_product_detail AS RSPD JOIN req_stockin_product_status AS RSPS 
#                                 ON RSPD.request_id = RSPS.request_id
#                                 JOIN product_detail as PD 
#                                 ON PD.product_id = RSPD.product_id
#                                 LEFT JOIN product_stock_in_real_details AS PSIRD 
#                                 ON RSPD.request_id = PSIRD.req_stockin_product_id AND RSPD.product_id = PSIRD.product_id
#                 WHERE RSPD.deleted_at IS NULL
#                         AND RSPS.deleted_at IS NULL
#                         AND RSPS.status NOT LIKE 'review'
#                         AND PD.deleted_at IS NULL
#                         AND PSIRD.deleted_at IS NULL
#         """)

# dfReqStockInProductStatus = pd.DataFrame([item.__dict__ for item in dfReqStockInProductStatus]).drop(['_state', 'id'], axis=1)
# print(dfReqStockInProductStatus)
# dfReqStockInProductStatus.to_csv('data_csv/ReqStockInProductStatus.csv', index= False)



# dfProductStockInRealDetails = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, PSIRD.quantity AS quantity_in_stock
#                 FROM product_detail AS PD JOIN product_stock_in_real_details AS PSIRD 
#                                 ON PD.product_id = PSIRD.product_id

#                 WHERE PD.deleted_at IS NULL
#                         AND PSIRD.deleted_at IS NULL
#                 ORDER BY PD.product_id ASC
#         """)

# dfProductStockInRealDetails = pd.DataFrame([item.__dict__ for item in dfProductStockInRealDetails]).drop(['_state', 'id'], axis=1)
# print(dfProductStockInRealDetails)
# dfProductStockInRealDetails.to_csv('data_csv/ProductStockInRealDetails.csv', index= False)



# dfProductionStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, PSO.quantity AS quantity_stock_out
#                 FROM product_detail AS PD JOIN production_stock_out AS PSO 
#                                 ON PD.product_id = PSO.product_id

#                 WHERE PD.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                 ORDER BY PD.product_id ASC
#         """)

# dfProductionStockOut = pd.DataFrame([item.__dict__ for item in dfProductionStockOut]).drop(['_state', 'id'], axis=1)
# print(dfProductionStockOut)
# dfProductionStockOut.to_csv('data_csv/ProductionStockOut.csv', index= False)




# dfOutSourcingQuota= ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, SUM(OQ.total_quota) AS total_quota
#                 FROM outsourcing_quota AS OQ JOIN product_detail AS PD 
#                                 ON PD.product_id = OQ.product_id
                                
#                 WHERE PD.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
#                 GROUP BY PD.product_id
#                 ORDER BY PD.product_id ASC
#         """)

# dfOutSourcingQuota = pd.DataFrame([item.__dict__ for item in dfOutSourcingQuota]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingQuota)
# dfOutSourcingQuota.to_csv('data_csv/OutSourcingQuota.csv', index= False)


# dfOutSourcingStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.product_id, OQ.outsourcing_order_id , OQ.total_quota AS quantity_outsourcing, OQ.is_exported, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_outsourcing
#                 FROM outsourcing_quota AS OQ 
#                         LEFT JOIN assign_product_stockout AS APS
#                             ON OQ.outsourcing_order_id = APS.outsourcing_order_id AND APS.outsourcing_quota_id = OQ.id 
                            
#                         LEFT JOIN production_stock_out AS PSO
#                                         ON PSO.product_id = OQ.product_id AND PSO.assign_product_stockout_id = APS.id
                            
#                 WHERE OQ.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                 ORDER BY OQ.product_id ASC;
#         """)
# dfOutSourcingStockOut = pd.DataFrame([item.__dict__ for item in dfOutSourcingStockOut]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingStockOut)
# dfOutSourcingStockOut.to_csv('data_csv/OutSourcingStockOut.csv', index= False)


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


# ## dfOutSourcingStockIn
# dfOutSourcingStockIn = ProductDetail.objects.raw(""" 
#         SELECT 1 id, OD.product_id AS outsourcing_product_id , OD.outsourcing_order_id, OD.quantity AS quantity_outsourcing_detail ,PSIRD.quantity AS quantity_stock_in
#                 FROM outsourcing_detail OD LEFT JOIN product_stock_in_real_details AS PSIRD 
#                                 ON OD.outsourcing_order_id = PSIRD.outsourcing_order_id AND OD.product_id = PSIRD.product_id

#                 WHERE OD.deleted_at IS NULL  
#                         AND PSIRD.deleted_at IS NULL
                        
#                 ORDER BY `OD`.`outsourcing_order_id` ASC;
#         """)

# dfOutSourcingStockIn = pd.DataFrame([item.__dict__ for item in dfOutSourcingStockIn]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingStockIn)
# dfOutSourcingStockIn.to_csv('data_csv/OutSourcingStockIn.csv', index= False)
