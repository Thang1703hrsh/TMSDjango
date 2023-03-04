# from .models_data import *
# import pandas as pd

# dfProductionNotExistOrder = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM production_not_exist_order PNEO
#         WHERE PNEO.deleted_at IS NULL
#         """)

# dfProductionNotExistOrder = pd.DataFrame([item.__dict__ for item in dfProductionNotExistOrder]).drop(['_state'], axis=1)
# print(dfProductionNotExistOrder)
# dfProductionNotExistOrder.to_csv('../data_csv/ProductionNotExistOrder.csv', index= False)

