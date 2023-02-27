from .models_data import *
import pandas as pd

dfOrderDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM order_detail OD
        WHERE OD.deleted_at IS NULL
        """)

dfOrderDetail = pd.DataFrame([item.__dict__ for item in dfOrderDetail]).drop(['_state', 'id'], axis=1)
print(dfOrderDetail)
dfOrderDetail.to_csv('../data_csv/OrderDetail.csv', index= False)


dfProductionNotExistOrder = ProductDetail.objects.raw("""  
        SELECT *
        FROM production_not_exist_order PNEO
        WHERE PNEO.deleted_at IS NULL
        """)

dfProductionNotExistOrder = pd.DataFrame([item.__dict__ for item in dfProductionNotExistOrder]).drop(['_state', 'id'], axis=1)
print(dfProductionNotExistOrder)
dfProductionNotExistOrder.to_csv('../data_csv/ProductionNotExistOrder.csv', index= False)


