# from .models import *
# import pandas as pd


# # def dfProductUnit():
# dfProductUnit = ProductDetail.objects.raw("""  
#         SELECT 1 id, PU.product_id , PU.id AS product_unit_id, PU.unit_id, units.name AS name_unit ,PU.is_default
#         FROM product_unit AS PU JOIN product_detail AS PD 
#                 ON PD.product_id = PU.product_id
#                 JOIN units ON PU.unit_id = units.id
#         WHERE PU.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL 
#                 AND units.deleted_at IS NULL 
            
#         """)
# dfProductUnit = pd.DataFrame([item.__dict__ for item in dfProductUnit]).drop(['_state', 'id'], axis=1)
# print(dfProductUnit)
# dfProductUnit.to_csv('dataDA/ProductUnit.csv', index= False)



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
# dfProductUnitExchange.to_csv('dataDA/ProductUnitExchange.csv', index= False)


# dfProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id , PD.code as product_code , PD.name ,PD.quantity AS quantity_product , PD.is_outsourcing
#         FROM product_detail PD 
#         WHERE PD.deleted_at IS NULL 
#                 AND PD.in_trash != 1
#         ORDER BY PD.product_id ASC
#         """)
# dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)
# print(dfProduct)
# dfProduct.to_csv('dataDA/Product.csv', index= False)


# ## Outsourcing 
# dfOutSourcingOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, OI.code , OI.outsourcing_order_id , OI.name, OI.is_complete AS is_complete_infos
#                 FROM outsourcing_infos OI JOIN outsourcing_orders OO 
#                         ON OO.id = OI.outsourcing_order_id
#                 WHERE OI.deleted_at IS NULL  
#                     AND OO.deleted_at IS NULL  
                        
#                 ORDER BY `OO`.`id` DESC;
#         """)

# dfOutSourcingOrder = pd.DataFrame([item.__dict__ for item in dfOutSourcingOrder]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingOrder)
# dfOutSourcingOrder.to_csv('dataDA/OutSourcingOrderBao.csv', index= False)


# ## dfOutSourcing Material
# dfOutSourcingMaterial = ProductDetail.objects.raw(""" 
#         SELECT 1 id, OQ.outsourcing_detail_id, OD.product_id AS outsourcing_product_id , OD.outsourcing_order_id, OD.quantity AS quantity_outsourcing_detail, OD.is_complete AS is_complete_detail , OQ.product_id , OQ.total_quota, OQ.is_exported ,OQ.quota_percent  
#                 FROM outsourcing_detail AS OD RIGHT JOIN outsourcing_quota AS OQ 
#                                 ON OQ.outsourcing_detail_id = OD.id AND OQ.outsourcing_order_id = OD.outsourcing_order_id
#                                 JOIN outsourcing_orders OO 
#                         ON OO.id = OD.outsourcing_order_id
#                 WHERE OD.deleted_at IS NULL  
#                         AND OQ.deleted_at IS NULL  
#                         AND OO.deleted_at IS NULL  
                        
#                 ORDER BY `OD`.`outsourcing_order_id` ASC;
#         """)

# dfOutSourcingMaterial = pd.DataFrame([item.__dict__ for item in dfOutSourcingMaterial]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingMaterial)
# dfOutSourcingMaterial.to_csv('dataDA/OutSourcingMaterialBao.csv', index= False)


# dfProductionOrder = ProductDetail.objects.raw("""  
# SELECT 1 id, PD.code AS product_code, POD.order_id, POD.production_order_id , POI.code AS production_code , POD.quantity AS quantity_production_order,  PSO.quantity AS quantity_exported_production_order , (CAST(POI.created_at AS DATE)) AS time_create, POI.completed_at , (CAST(PSO.created_at AS DATE)) AS time_stock_out
#         FROM production_order_detail AS POD 
#                 JOIN product_detail AS PD 
#                         ON PD.product_id = POD.product_id
#                 JOIN production_order_info AS POI 
#                         ON POI.production_order_id = POD.production_order_id 
#                 LEFT JOIN assign_product_stockout AS APS
#                         ON POD.production_order_id = APS.production_order_id AND APS.production_order_detail_id = POD.id
                        
#                 LEFT JOIN production_stock_out AS PSO
#                         ON PSO.product_id = POD.product_id AND PSO.assign_product_stockout_id = APS.id 
                    
#         WHERE POD.deleted_at IS NULL
#                 AND PSO.deleted_at IS NULL
#                 AND APS.deleted_at IS NULL
#                 AND PD.deleted_at IS NULL
#                 AND POI.deleted_at IS NULL
#         ORDER BY POD.order_id ASC
# """)
# dfProductionOrder = pd.DataFrame([item.__dict__ for item in dfProductionOrder]).drop(['_state', 'id'], axis=1)
# print(dfProductionOrder)
# dfProductionOrder.to_csv('dataDA/ProductionOrderDetailBao.csv', index= False)


# dfOrder = ProductDetail.objects.raw("""  
# SELECT 1 id, OD.code AS order_code ,OQ.order_id, OQ.product_id, OQ.position ,PD.code AS product_code ,OQ.total_quota
#         FROM order_quota AS OQ JOIN product_detail PD 
#                 ON OQ.product_id = PD.product_id
#         JOIN order_detail AS OD 
#                 ON OD.order_id = OQ.order_id
        
#         WHERE OQ.deleted_at IS NULL
#                 AND PD.deleted_at IS NULL
#                 AND OD.deleted_at IS NULL
#         ORDER BY OQ.order_id ASC;
# """)
# dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)
# print(dfOrder)
# dfOrder.to_csv('dataDA/OrderBao.csv', index= False)



# dfOutsourcingStockIn = ProductDetail.objects.raw("""  
#         SELECT 1 id, OD.outsourcing_order_id ,OD.product_id, OD.quantity AS outsourcing_quantity ,PSIRD.quantity_stock_in AS quantity_stock_in , (CAST(PSIRD.created_at AS DATE)) AS delivery_real_
#                 FROM outsourcing_detail OD LEFT JOIN (SELECT PSIRD.product_id, PSIRD.outsourcing_order_id, PSIRD.created_at, SUM(PSIRD.quantity) AS quantity_stock_in
#                                                 FROM product_stock_in_real_details AS PSIRD 
#                                                 WHERE PSIRD.deleted_at IS NULL  
#                                                 GROUP BY PSIRD.product_id, PSIRD.outsourcing_order_id, PSIRD.created_at) AS PSIRD
#                                         ON OD.outsourcing_order_id = PSIRD.outsourcing_order_id AND OD.product_id = PSIRD.product_id
#                                         JOIN outsourcing_orders OO ON OO.id = OD.outsourcing_order_id
#                 WHERE OD.deleted_at IS NULL  
#                         AND OO.deleted_at IS NULL  
#                 ORDER BY `OD`.`outsourcing_order_id` DESC; 
#         """)

# dfOutsourcingStockIn = pd.DataFrame([item.__dict__ for item in dfOutsourcingStockIn]).drop(['_state', 'id'], axis=1)
# print(dfOutsourcingStockIn)
# dfOutsourcingStockIn.to_csv('dataDA/OutsourcingStockInBao.csv', index= False)


# ## Outsourcing Detail
# dfOutSourcingDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, OI.outsourcing_order_id , OI.code ,OI.name, OI.is_complete AS is_complete_order, (CAST(OI.created_at AS DATE)) AS created_at_ , (CAST(OI.delivery_at AS DATE)) AS delivery_at_, OD.product_id ,OD.quantity AS outsourcing_quantity , OD.is_complete AS is_complete_order_detail
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
# dfOutSourcingDetail.to_csv('dataDA/OutSourcingDetailBao.csv', index= False)



# # ## OutSourcing StockOut
# dfOutSourcingStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.product_id, OQ.outsourcing_order_id , OQ.is_exported, OQ.outsourcing_detail_id, OQ.outsourcing_detail_id ,PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_outsourcing , (CAST(PSO.created_at AS DATE)) AS date_of_inventory
#                 FROM outsourcing_quota AS OQ 
#                         LEFT JOIN assign_product_stockout AS APS
#                                 ON OQ.outsourcing_order_id = APS.outsourcing_order_id AND APS.outsourcing_quota_id = OQ.id 
#                         LEFT JOIN production_stock_out AS PSO
#                                 ON PSO.product_id = OQ.product_id AND PSO.assign_product_stockout_id = APS.id
#                         JOIN outsourcing_orders OO 
#                                 ON OO.id = OQ.outsourcing_order_id
                            
#                 WHERE OQ.deleted_at IS NULL
#                         AND PSO.deleted_at IS NULL
#                         AND APS.deleted_at IS NULL
#                         AND APS.outsourcing_order_id IS NOT NULL
#                         AND OO.deleted_at IS NULL
#                 ORDER BY OQ.product_id ASC;
#         """)
# dfOutSourcingStockOut = pd.DataFrame([item.__dict__ for item in dfOutSourcingStockOut]).drop(['_state', 'id'], axis=1)
# print(dfOutSourcingStockOut)
# dfOutSourcingStockOut.to_csv('dataDA/OutSourcingStockOutBao.csv', index= False)



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
# dfRelationship.to_csv('dataDA/Relationship.csv', index= False)




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


