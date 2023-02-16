# from .models import *
# import pandas as pd


# # Request stockin product status
# dfReqStockInProduct= ProductDetail.objects.raw("""  
#         SELECT 1 id, RSP.id as request_id, RSPS.status, RSP.is_complete AS complete_req,  RSPI.code AS req_code, RSPI.reason ,  RSPD.product_id , RSPD.quantity, RSPD.is_complete AS complete_detail
#                 FROM req_stockin_product AS RSP JOIN req_stockin_product_status AS RSPS 
#                                 ON RSPS.request_id = RSP.id
#                                 JOIN req_stockin_product_info as RSPI  
#                                 ON RSPI.request_id = RSP.id
#                                 JOIN req_stockin_product_detail AS RSPD
#                                 ON RSPD.request_id = RSP.id
#                 WHERE RSPD.deleted_at IS NULL
#                         AND RSPS.deleted_at IS NULL
#                         AND RSP.deleted_at IS NULL
#                         AND RSPI.deleted_at IS NULL 
                
#         """)

# dfReqStockInProduct = pd.DataFrame([item.__dict__ for item in dfReqStockInProduct]).drop(['_state', 'id'], axis=1)
# print(dfReqStockInProduct)
# dfReqStockInProduct.to_csv('data_csv/ReqStockInProduct.csv', index= False)



# # Request stockin product status
# dfReqStockInProductStatus= ProductDetail.objects.raw("""  
#         SELECT 1 id, PSIRD.product_id, PSIRD.req_stockin_product_id AS request_id, PSIRD.quantity AS quantity_in_stock_by_req
#                 FROM product_stock_in_real_details AS PSIRD 
#                 WHERE PSIRD.deleted_at IS NULL
#                         AND PSIRD.req_stockin_product_id IS NOT NULL
#         """)

# dfReqStockInProductStatus = pd.DataFrame([item.__dict__ for item in dfReqStockInProductStatus]).drop(['_state', 'id'], axis=1)
# print(dfReqStockInProductStatus)
# dfReqStockInProductStatus.to_csv('data_csv/ReqStockInProductStatus.csv', index= False)
