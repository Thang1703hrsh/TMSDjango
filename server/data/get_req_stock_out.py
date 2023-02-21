
# from .models_data import *
# import pandas as pd


# # Req stockout product 
# dfReqStockoutProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPI.request_id, RSP.creator_id ,RSPI.code AS req_stockout_code, RSPI.reason ,RSPS.status AS req_stockout_status, RSP.is_complete AS is_complete_req , (CAST(RSP.updated_at AS DATE)) AS time_create
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
# dfReqStockoutProduct.to_csv('../data_csv/ReqStockoutProduct.csv', index= False)



# # Req stockout product detail + Assign product stock + production_stock_out 
# dfReqStockoutProductStockOut = ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id,RSPD.request_id, RSPD.is_exported, RSPD.is_complete AS is_complete_req_detail ,RSPD.quantity AS quantity_req_stockout, PSO.assign_product_stockout_id, PSO.quantity AS quantity_exported_req_stockout , PSO.creator_id, (CAST(PSO.updated_at AS DATE)) AS time_stock_out
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
# dfReqStockoutProductStockOut.to_csv('../data_csv/ReqStockoutProductStockOut.csv', index= False)

