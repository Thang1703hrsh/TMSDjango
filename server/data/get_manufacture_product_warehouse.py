# from .models_data import *
# import pandas as pd

# ## Outsourcing Stock In Detail
# dfManuProdWarehouse = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM manufacture_product_warehouse MPW
#         WHERE MPW.deleted_at IS NULL
#         """)

# dfManuProdWarehouse = pd.DataFrame([item.__dict__ for item in dfManuProdWarehouse]).drop(['_state'], axis=1)
# print(dfManuProdWarehouse)
# dfManuProdWarehouse.to_csv('../data_csv/ManuProdWarehouse.csv', index= False)
