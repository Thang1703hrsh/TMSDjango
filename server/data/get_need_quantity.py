
# from .models import *
# import pandas as pd


# dfOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.order_id, OQ.product_id, PD.code AS product_code, OS.status AS order_status,OQ.position ,OQ.total_quota, OD.is_complete AS complete_order, OBS.status AS booking_status
#                 FROM order_quota AS OQ JOIN product_detail PD 
#                             ON OQ.product_id = PD.product_id
#                         JOIN order_status AS OS
#                             ON OS.order_id = OQ.order_id
#                         JOIN orders 
#                             ON orders.id = OQ.order_id
#                         JOIN order_booking AS OB
#                             ON OB.order_id = OQ.order_id
#                         JOIN order_detail AS OD
#                             ON OD.order_id = OQ.order_id
#                         JOIN order_booking_status AS OBS
#                             ON OBS.order_booking_id = OQ.order_booking_id

#                 WHERE OQ.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
#                         AND OS.deleted_at IS NULL
#                         AND orders.deleted_at IS NULL
#                         AND OB.deleted_at IS NULL
#                         AND OD.deleted_at IS NULL
#                         AND OBS.deleted_at IS NULL
  
#                 ORDER BY OS.order_id ASC;
#         """)
# dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)
# print(dfOrder)
# dfOrder.to_csv('data_csv/Order.csv', index= False)



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


# # Production order detail + Assign product stock + production_stock_out
# dfProductionOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, POS.production_order_id, POS.status AS production_status
#                 FROM production_orders AS PO JOIN production_order_status AS POS 
#                         ON PO.id = POS.production_order_id

#                         JOIN production_order_info AS POI
#                         ON POI.production_order_id = POS.production_order_id 
        
                            
#                 WHERE PO.deleted_at IS NULL
#                         AND POS.deleted_at IS NULL
#                         AND POI.deleted_at IS NULL
                        
#                 ORDER BY POS.production_order_id ASC;
#         """)
# dfProductionOrder = pd.DataFrame([item.__dict__ for item in dfProductionOrder]).drop(['_state', 'id'], axis=1)
# print(dfProductionOrder)
# dfProductionOrder.to_csv('data_csv/ProductionOrder.csv', index= False)



# dfProductionDetailStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, POD.product_id, POD.order_id, POD.production_order_id , POD.is_complete AS complete_prodtion_stockout , POD.is_exported ,POD.quantity AS quantity_production_order, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_production_order
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
# dfProductionDetailStockOut = pd.DataFrame([item.__dict__ for item in dfProductionDetailStockOut]).drop(['_state', 'id'], axis=1)
# print(dfProductionDetailStockOut)
# dfProductionDetailStockOut.to_csv('data_csv/ProductionDetailStockOut.csv', index= False)


# # Req stockout product 
# dfReqStockoutProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPI.request_id, RSPI.code AS req_stockout_code, RSPS.status AS req_stockout_status, RSP.is_complete AS is_complete_req
#                 FROM req_stockout_product RSP JOIN req_stockout_product_info RSPI
#                                 ON RSP.id = RSPI.request_id
                
#                         JOIN req_stockout_product_status RSPS
#                                 ON RSP.id = RSPS.request_id
                                
#                 WHERE RSP.deleted_at IS NULL
#                         AND RSPI.deleted_at IS NULL
#                         AND RSPS.deleted_at IS NULL
#                 ORDER BY RSPI.request_id ASC;

#         """)

# dfReqStockoutProduct = pd.DataFrame([item.__dict__ for item in dfReqStockoutProduct]).drop(['_state', 'id'], axis=1)
# print(dfReqStockoutProduct)
# dfReqStockoutProduct.to_csv('data_csv/ReqStockoutProduct.csv', index= False)


# # Req stockout product detail + Assign product stock + production_stock_out
# dfReqStockoutProductStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id,RSPD.request_id, RSPD.is_exported, RSPD.is_complete AS is_complete_req_detail ,RSPD.quantity AS quantity_req_stockout, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_req_stockout
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

# dfReqStockoutProductStockOut = pd.DataFrame([item.__dict__ for item in dfReqStockoutProductStockOut]).drop(['_state', 'id'], axis=1)
# print(dfReqStockoutProductStockOut)
# dfReqStockoutProductStockOut.to_csv('data_csv/ReqStockoutProductStockOut.csv', index= False)



# # req material offset production
# dfReqMaterialOffsetProduction = ProductDetail.objects.raw("""  
#         SELECT 1 id, RMOPS.request_id, RMOP.code, RMOP.production_order_id , RMOPS.status
#                 FROM req_material_offset_production AS RMOP 
#                         JOIN req_material_offset_production_status AS RMOPS
#                             ON RMOP.id = RMOPS.request_id 
                            
#                 WHERE RMOP.deleted_at IS NULL
#                         AND RMOPS.deleted_at IS NULL
#                 ORDER BY RMOP.id ASC;
#         """)
# dfReqMaterialOffsetProduction = pd.DataFrame([item.__dict__ for item in dfReqMaterialOffsetProduction]).drop(['_state', 'id'], axis=1)
# print(dfReqMaterialOffsetProduction)
# dfReqMaterialOffsetProduction.to_csv('data_csv/ReqMaterialOffsetProduction.csv', index= False)


# # req material offset production detail + Assign product stock + production_stock_out
# dfReqMaterialOffsetProductionStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, RMOPD.product_id, RMOPD.order_id, RMOPD.request_id ,RMOPD.production_order_id, RMOPD.is_exported ,RMOPD.quantity AS quantity_req_material_offset_production, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_req_material_offset_production
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
# dfReqMaterialOffsetProductionStockOut = pd.DataFrame([item.__dict__ for item in dfReqMaterialOffsetProductionStockOut]).drop(['_state', 'id'], axis=1)
# print(dfReqMaterialOffsetProductionStockOut)
# dfReqMaterialOffsetProductionStockOut.to_csv('data_csv/ReqMaterialOffsetProductionStockOut.csv', index= False)




# dfReturnProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RPD.return_product_id, RP.code ,RPD.product_id, RPD.product_unit_id, RP.is_outsourcing ,RP.qrcode, RP.is_exported, RP.is_complete AS is_complete_return
#                 FROM return_products AS RP JOIN return_product_detail AS RPD
#                         ON RP.id = RPD.return_product_id 

#                 WHERE RP.deleted_at IS NULL
#                         AND RPD.deleted_at IS NULL
                        
#                 ORDER BY RPD.return_product_id ASC
#         """)

# dfReturnProduct = pd.DataFrame([item.__dict__ for item in dfReturnProduct]).drop(['_state', 'id'], axis=1)
# print(dfReturnProduct)
# dfReturnProduct.to_csv('data_csv/ReturnProduct.csv', index= False)


# dfReturnProductStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, RPD.product_id, RPD.product_unit_id ,RPD.return_product_id, RPD.quantity AS quantity_return_product, RPD.purchase_order_id, RPD.outsourcing_order_id ,RPD.is_complete AS is_complete_return_detail ,PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_return_product
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

# dfReturnProductStockOut = pd.DataFrame([item.__dict__ for item in dfReturnProductStockOut]).drop(['_state', 'id'], axis=1)
# print(dfReturnProductStockOut)
# dfReturnProductStockOut.to_csv('data_csv/ReturnProductStockOut.csv', index= False)


# ## request_material_offset
# dfRequestMaterialOffset = ProductDetail.objects.raw("""  
#         SELECT 1 id, MODD.material_offset_id, MODD.order_id ,MODD.product_id, MODD.total_quota, RMOS.status AS req_mat_offset_status
#             FROM request_material_offset AS RMO 
#                     JOIN request_material_offset_status AS RMOS 
#                             ON RMO.id = RMOS.request_id
#                     JOIN material_offset_detail AS MODD
#                             ON RMO.id = MODD.material_offset_id
#             WHERE RMO.deleted_at IS NULL
#                     AND RMOS.deleted_at IS NULL
#                     AND MODD.deleted_at IS NULL
#             ORDER BY MODD.material_offset_id ASC;
#         """)

# dfRequestMaterialOffset = pd.DataFrame([item.__dict__ for item in dfRequestMaterialOffset]).drop(['_state', 'id'], axis=1)
# print(dfRequestMaterialOffset)
# dfRequestMaterialOffset.to_csv('data_csv/RequestMaterialOffset.csv', index= False)

