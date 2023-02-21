from .models_data import *
import pandas as pd


dfProduct = ProductDetail.objects.raw("""  
        SELECT 1 id, PD.product_id , PD.code as product_code , PD.name ,PD.quantity AS quantity_product , PD.is_outsourcing
        FROM product_detail PD 
        WHERE PD.deleted_at IS NULL 
                AND PD.in_trash != 1
        ORDER BY PD.product_id ASC
        """)
dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)
print(dfProduct)
dfProduct.to_csv('../data_csv/Product.csv', index= False)
