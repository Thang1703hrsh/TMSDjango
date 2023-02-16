# from .models import *
# import pandas as pd

# # purchase order
# dfPurchaseOrder= ProductDetail.objects.raw("""  
#         SELECT 1 id, POD.code , POD.name AS name_po, POD.creator_id ,POD.total_amount , POD.purchase_order_id , POD.is_completed, POS.status as po_status, (CAST(PO.updated_at AS DATE)) AS time_create , (CAST(POD.delivery_at AS DATE)) AS estimated_delivery
#                 ,  POD.supplier_delivery_id , POD.creator_id
#                 FROM purchase_order_detail AS POD JOIN purchase_orders AS PO
#                                 ON PO.id = POD.purchase_order_id
#                     JOIN purchase_order_status POS 
#                                 ON PO.id = POS.purchase_order_id
        
#                 WHERE POD.deleted_at IS NULL
#                         AND PO.deleted_at IS NULL
#                         AND POS.deleted_at IS NULL
                
#         """)

# dfPurchaseOrder = pd.DataFrame([item.__dict__ for item in dfPurchaseOrder]).drop(['_state', 'id'], axis=1)
# print(dfPurchaseOrder)
# dfPurchaseOrder.to_csv('../data_csv/PurchaseOrder.csv', index= False)



# # purchase order detail
# dfPurchaseOrderDetail= ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.code AS product_code, PD.product_id, PL.product_unit_id ,PL.quantity AS purchase_order_quantity, PL.purchase_order_id, PL.is_complete 
#                 FROM product_detail AS PD  JOIN packing_list AS PL 
#                                                 ON PD.product_id = PL.product_id
    
#                 WHERE PL.deleted_at IS NULL
#                         AND PD.deleted_at IS NULL
#                 ORDER BY PD.product_id ASC
#         """)

# dfPurchaseOrderDetail = pd.DataFrame([item.__dict__ for item in dfPurchaseOrderDetail]).drop(['_state', 'id'], axis=1)
# print(dfPurchaseOrderDetail)
# dfPurchaseOrderDetail.to_csv('../data_csv/PurchaseOrderDetail.csv', index= False)


# # # enter the inventory of the purchase order
# # dfStockInPurchaseOrder= ProductDetail.objects.raw("""  
# #         SELECT 1 id, PL.purchase_order_id , PL.product_id, PSIRT.product_unit_id ,SUM(PSIRT.quantity) AS quantity_arrived
# #                 FROM packing_list AS PL LEFT JOIN product_stock_in_real_details AS PSIRT 
# #                         ON PL.product_id = PSIRT.product_id AND PL.purchase_order_id = PSIRT.purchase_order_id

# #                 WHERE PL.deleted_at IS NULL
# #                         AND PSIRT.deleted_at IS NULL

# #                 GROUP BY PL.purchase_order_id , PL.product_id, PSIRT.product_unit_id

# #         """)

# # dfStockInPurchaseOrder = pd.DataFrame([item.__dict__ for item in dfStockInPurchaseOrder]).drop(['_state', 'id'], axis=1)
# # print(dfStockInPurchaseOrder)
# # dfStockInPurchaseOrder.to_csv('data_csv/StockInPurchaseOrder.csv', index= False)

# # enter the inventory of the purchase order
# dfStockInPurchaseOrder= ProductDetail.objects.raw("""  
#         SELECT 1 id, PSIRT.product_id , PSIRT.purchase_order_id ,SUM(PSIRT.quantity) AS quantity_arrived, (CAST(PSIRT.updated_at AS DATE)) AS actual_delivery_time 
#                 FROM product_stock_in_real_details AS PSIRT 

#                 WHERE PSIRT.deleted_at IS NULL
#                     AND purchase_order_id IS NOT NULL

#                 GROUP BY PSIRT.product_id, PSIRT.product_unit_id, PSIRT.purchase_order_id , PSIRT.updated_at
#                 ORDER BY PSIRT.purchase_order_id ASC

#         """)

# dfStockInPurchaseOrder = pd.DataFrame([item.__dict__ for item in dfStockInPurchaseOrder]).drop(['_state', 'id'], axis=1)
# print(dfStockInPurchaseOrder)
# dfStockInPurchaseOrder.to_csv('../data_csv/StockInPurchaseOrder.csv', index= False)
