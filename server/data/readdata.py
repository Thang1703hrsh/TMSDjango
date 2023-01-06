# from .models import *
# import pandas as pd

# # def readdfOrder():
# dfOrder = OrderQuota.objects.raw("""  
#         SELECT 1 id, PD.product_id AS parent_product, OD.code as order_code , OQ.position, PD.code as product_code ,OQ.quota as order_quota, OQ.total_quota, POD.quantity as production_order_quantity ,PSO.quantity_stock_out
#         FROM order_quota AS OQ JOIN order_detail AS OD 
#                                         ON OQ.order_id = OD.order_id 
#                                 JOIN product_detail AS PD 
#                                         ON OQ.product_id = PD.product_id  
#                                 LEFT JOIN (SELECT PSO.product_id, PSO.order_id, SUM(PSO.quantity) AS quantity_stock_out
#                                                 FROM production_stock_out AS PSO 
#                                                 WHERE PSO.deleted_at IS NULL  
#                                                 GROUP BY PSO.product_id, PSO.order_id) AS PSO
#                                         ON OQ.product_id = PSO.product_id AND OQ.order_id = PSO.order_id
#                                 LEFT JOIN production_order_detail AS POD  
#                                         ON OQ.product_id = POD.product_id AND OQ.order_id = POD.order_id
#                                 JOIN order_status AS OS
#                                         ON OQ.order_id = OS.order_id
#         WHERE OD.deleted_at IS NULL 
#                 AND OQ.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL
#                 AND OS.status LIKE 'approval'
#                 AND OS.deleted_at IS NULL
#                 AND POD.deleted_at IS NULL
#         ORDER BY OD.order_id DESC
#         """)
# dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)
# print(dfOrder)
# dfOrder.to_csv('data_csv/Order.csv', index= False)

# # return dfOrder

# dfOrderQuota = OrderQuota.objects.raw("""  
#         SELECT 1 id, PD.product_id AS parent_product, OD.code as order_code , OQ.position, PD.code as product_code ,OQ.quota as order_quota, OQ.total_quota
#         FROM order_quota AS OQ JOIN order_detail AS OD 
#                                         ON OQ.order_id = OD.order_id 
#                                 JOIN product_detail AS PD ON 
#                                         OQ.product_id = PD.product_id  
                                
#         WHERE OD.deleted_at IS NULL 
#                 AND OQ.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL

#         ORDER BY OD.order_id DESC
#         """)
# dfOrderQuota = pd.DataFrame([item.__dict__ for item in dfOrderQuota]).drop(['_state', 'id'], axis=1)
# print(dfOrderQuota)
# dfOrderQuota.to_csv('data_csv/OrderQuota.csv', index= False)

# # return dfOrderQuota

# # Production_Order_Detail and production_stock_out

# dfProductionOrderDetail = ProductDetail.objects.raw("""  
#         SELECT 1 id, POD.product_id, POD.order_id, POD.quantity_production_order, PSO.quantity_stock_out
#         FROM (SELECT POD.product_id, POD.order_id, SUM(POD.quantity) AS quantity_production_order
#                         FROM production_order_detail AS POD 
#                         WHERE POD.deleted_at IS NULL  
#                         GROUP BY POD.product_id, POD.order_id) AS POD JOIN (SELECT PSO.product_id, PSO.order_id, SUM(PSO.quantity) AS quantity_stock_out
#                                                 FROM production_stock_out AS PSO 
#                                                 WHERE PSO.deleted_at IS NULL  
#                                                 GROUP BY PSO.product_id, PSO.order_id) AS PSO
#                                         ON PSO.product_id = POD.product_id AND PSO.order_id = POD.order_id
                                        
#         ORDER BY POD.order_id ASC
#         """)
# dfProductionOrderDetail = pd.DataFrame([item.__dict__ for item in dfProductionOrderDetail]).drop(['_state', 'id'], axis=1)
# print(dfProductionOrderDetail)
# dfProductionOrderDetail.to_csv('data_csv/ProductionOrderDetail.csv', index= False)



# # def readdfChild():
# dfChild = OutsourcingProductMaterials.objects.raw("""  
#         SELECT 1 id, OPM.outsourcing_product_id AS parent_product, OPM.product_id AS child_product, PD.code as product_code , OPM.quantity as quota
#         FROM outsourcing_product_materials AS OPM JOIN product_detail AS PD 
#                                         ON OPM.product_id = PD.product_id 
#         WHERE OPM.deleted_at IS NULL 
#         AND PD.deleted_at IS NULL 
        
#         """)
# dfChild = pd.DataFrame([item.__dict__ for item in dfChild]).drop(['_state', 'id'], axis=1)

# print(dfChild)
# # print(dfChild.dtypes)
# dfChild.to_csv('data_csv/Child.csv', index= False)

#         # return dfChild



# # def readdfParent():

# dfParent = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id AS parent_product, PD.code as product_code , PD.quantity AS product_quantity, MR.temporary_quantity , PD.is_outsourcing
#         FROM ttdbeta_data.product_detail PD JOIN ttdbeta_report.material_reports MR
#                                         ON PD.product_id = MR.product_id 
#         WHERE MR.deleted_at IS NULL 
#         AND PD.deleted_at IS NULL 
#         ORDER BY PD.product_id ASC
#         """)
# dfParent = pd.DataFrame([item.__dict__ for item in dfParent]).drop(['_state', 'id'], axis=1)
#         # return dfParent
# print(dfParent)
# # print(dfParent.dtypes)
# dfParent.to_csv('data_csv/Parent.csv', index= False)




# # dfOrder = OrderQuota.objects.raw("""  
# #         SELECT 1 id, OD.code as order_code , OQ.position, PD.code as product_code , OQ.total_quota, PSO.quantity as stockout_quantity
# #         FROM order_quota AS OQ JOIN order_detail AS OD 
# #                                         ON OQ.order_id = OD.order_id 
# #                                 JOIN product_detail AS PD ON 
# #                                         OQ.product_id = PD.product_id  
# #                                 LEFT JOIN production_stock_out AS PSO ON 
# #                                         OQ.product_id = PSO.product_id AND OQ.order_id = PSO.order_id
# #                                 JOIN order_status AS OS ON
# #                                         OQ.order_id = OS.order_id
# #         WHERE OD.deleted_at IS NULL 
# #                 AND OQ.deleted_at IS NULL 
# #                 AND PD.deleted_at IS NULL
# #                 AND PSO.deleted_at IS NULL
# #                 AND OS.status LIKE 'approval'
# #                 AND OS.deleted_at IS NULL
# #         ORDER BY OD.order_id ASC
        
# #         """)
# # dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)
# # print(dfOrder)
# # dfOrder.to_csv('Order.csv', index= False)


# # dfReqStockoutProductDetail = ProductDetail.objects.raw("""  
# #         SELECT 1 id, RSPD.product_id, RSPD.request_id, RSPD.quantity, RSPD.quantity* RSPD.is_exported AS exported_quantity , RSPD.is_exported, RSPD.is_complete
# #                 FROM req_stockout_product_detail RSPD JOIN product_detail PD
# #                                                 ON PD.product_id = RSPD.product_id 
# #                                                 JOIN req_stockout_product_info RSPI
# #                                                 ON RSPD.request_id = RSPI.request_id
                                                
# #                 WHERE RSPD.deleted_at IS NULL
# #                         AND PD.deleted_at IS NULL
# #                 AND RSPI.deleted_at IS NULL  
# #                 ORDER BY `RSPD`.`product_id` ASC;

# #         """)

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



# ## Request stock out product detail

# # dfReqStockoutProductDetail = ProductDetail.objects.raw("""  
# #         SELECT 1 id, RSPD.product_id, RSPD.request_id, RSPD.quantity AS quantity_req_stockout, APS.id AS assign_id
# #                 FROM req_stockout_product_detail RSPD JOIN assign_product_stockout APS
# #                                 ON RSPD.request_id = APS.req_stockout_prod_id

# #                 WHERE RSPD.deleted_at IS NULL
# #                         AND APS.deleted_at IS NULL
# #                         AND APS.req_stockout_prod_id IS NOT NULL  
# #                 ORDER BY `RSPD`.`product_id` ASC;

# #         """)

# # dfReqStockoutProductDetail = pd.DataFrame([item.__dict__ for item in dfReqStockoutProductDetail]).drop(['_state', 'id'], axis=1)
# # print(dfReqStockoutProductDetail)
# # dfReqStockoutProductDetail.to_csv('data_csv/ReqStockoutProductDetail.csv', index= False)



# # dfReqProductionStockout = ProductDetail.objects.raw("""  
# #         SELECT 1 id, PSO.product_id, PSO.assign_product_stockout_id, PSO.quantity AS quantity_stockout_by_req
# #                 FROM production_stock_out PSO JOIN assign_product_stockout APS
# #                                 ON PSO.assign_product_stockout_id = APS.id

# #                 WHERE PSO.deleted_at IS NULL
# #                         AND APS.deleted_at IS NULL
# #                         AND APS.req_stockout_prod_id IS NOT NULL  
# #                 ORDER BY `PSO`.`product_id` ASC;

# #         """)

# # dfReqProductionStockout = pd.DataFrame([item.__dict__ for item in dfReqProductionStockout]).drop(['_state', 'id'], axis=1)
# # print(dfReqProductionStockout)
# # dfReqProductionStockout.to_csv('data_csv/ReqProductionStockout.csv', index= False)



# ## Outsourcing Detail
# # dfOutSourcingDetail = ProductDetail.objects.raw("""  
# #         SELECT 1 id, OD.product_id, OD.outsourcing_order_id, OD.quantity AS outsourcing_quantity, PSIRD.quantity AS quantity_stock_in
# #                 FROM outsourcing_detail OD LEFT JOIN product_stock_in_real_details PSIRD 
# #                                                                 ON OD.outsourcing_order_id = PSIRD.outsourcing_order_id AND OD.product_id = PSIRD.product_id
# #                 WHERE OD.deleted_at IS NULL  
# #                         AND PSIRD.deleted_at IS NULL  
# #                 ORDER BY `OD`.`product_id` ASC

# #         """)

# # dfOutSourcingDetail = pd.DataFrame([item.__dict__ for item in dfOutSourcingDetail]).drop(['_state', 'id'], axis=1)
# # print(dfOutSourcingDetail)
# # dfOutSourcingDetail.to_csv('OutSourcingDetail.csv', index= False)

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






# # Request Return Product detail
# dfReturnProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RPD.product_id, SUM(RPD.quantity) AS return_request_quantity, SUM(PSO.quantity) AS returned_quantity
#                 FROM return_product_detail AS RPD LEFT JOIN production_stock_out AS PSO
#                                                         ON RPD.product_id = PSO.product_id AND RPD.product_unit_id = PSO.product_unit_id
#                                 JOIN assign_product_stockout APS 
#                                 ON APS.product_stock_out_id = PSO.product_stock_out_id AND APS.id = PSO.id

#                 WHERE PSO.deleted_at IS NULL
#                         AND RPD.deleted_at IS NULL
#                 AND APS.deleted_at IS NULL
#                 AND APS.return_product_id IS NOT NULL
#                 GROUP BY RPD.product_id
#                 ORDER BY RPD.product_id ASC
#         """)

# dfReturnProduct = pd.DataFrame([item.__dict__ for item in dfReturnProduct]).drop(['_state', 'id'], axis=1)
# print(dfReturnProduct)
# dfReturnProduct.to_csv('data_csv/ReturnProduct.csv', index= False)


# # purchase order

# dfPurchaseOrderDetail= ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, SUM(PL.quantity) AS purchase_order_quantity
#                 FROM product_detail AS PD  JOIN packing_list AS PL 
#                                                 ON PD.product_id = PL.product_id
    
#                 WHERE PL.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
#                 GROUP BY PD.product_id
#                 ORDER BY PD.product_id ASC
#         """)

# dfPurchaseOrderDetail = pd.DataFrame([item.__dict__ for item in dfPurchaseOrderDetail]).drop(['_state', 'id'], axis=1)
# print(dfPurchaseOrderDetail)
# dfPurchaseOrderDetail.to_csv('data_csv/PurchaseOrder.csv', index= False)


# # enter the inventory of the purchase order
# dfStockInPurchaseOrder= ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id, SUM(PSIRT.quantity) AS quantity_in_stock_by_purchase_order
#                 FROM product_detail AS PD  JOIN product_stock_in_real_details AS PSIRT 
#                                 ON PSIRT.product_id = PD.product_id

                                
#                 WHERE PD.deleted_at IS NULL
#                         AND PSIRT.purchase_order_id IS NOT NULL
#                         AND PSIRT.deleted_at IS NULL
#                 GROUP BY PD.product_id
#                 ORDER BY PD.product_id ASC
#         """)

# dfStockInPurchaseOrder = pd.DataFrame([item.__dict__ for item in dfStockInPurchaseOrder]).drop(['_state', 'id'], axis=1)
# print(dfStockInPurchaseOrder)
# dfStockInPurchaseOrder.to_csv('data_csv/StockInPurchaseOrder.csv', index= False)


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




# # dfOutSourcing= ProductDetail.objects.raw("""  
# #         SELECT 1 id, OI.outsourcing_order_id, OI.name, OQ.product_id, OQ.total_quota , OD.quantity as quantity_outsourcing_detail, PSIRD.quantity as quantity_stock_in 
# #                 FROM outsourcing_infos AS OI JOIN outsourcing_detail AS OD
# #                                         ON OI.outsourcing_order_id = OD.outsourcing_order_id
# #                                 JOIN product_stock_in_real_details AS PSIRD
# #                                         ON PSIRD.outsourcing_order_id = OI.outsourcing_order_id 
# #                                 JOIN outsourcing_quota AS OQ 
# #                                         ON OQ.outsourcing_order_id = OI.outsourcing_order_id AND PSIRD.product_id = OQ.product_id
                                
# #                 WHERE OI.deleted_at IS NULL
# #                         AND OD.deleted_at IS NULL
# #                         AND PSIRD.deleted_at IS NULL
# #                         AND PSIRD.outsourcing_order_id IS NOT NULL
# #                         AND OQ.deleted_at IS NULL
# #         """)

# # dfOutSourcing = pd.DataFrame([item.__dict__ for item in dfOutSourcing]).drop(['_state', 'id'], axis=1)
# # print(dfOutSourcing)
# # dfOutSourcing.to_csv('OutSourcing.csv', index= False)


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