# from .models import *
# import pandas as pd


# dfReqStockInProduct= ProductDetail.objects.raw("""  
#         SELECT 1 id, RSPD.product_id, RSPD.request_id, RSPD.quantity AS quantity_req_stockin, RSPD.is_complete AS is_complete_req_detail, RSP.is_complete AS is_complete_req
#                 FROM req_stockin_product AS RSP JOIN req_stockin_product_detail AS RSPD
#                                 ON RSP.id = RSPD.request_id

#                 WHERE RSP.deleted_at IS NULL
#                     AND RSPD.deleted_at IS NULL

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
