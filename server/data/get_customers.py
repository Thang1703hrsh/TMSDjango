from .models_data import *
import pandas as pd

dfCustomerDetail = ProductDetail.objects.raw("""  
        SELECT *
        FROM customer_detail CD
        WHERE CD.deleted_at IS NULL
        """)

dfCustomerDetail = pd.DataFrame([item.__dict__ for item in dfCustomerDetail]).drop(['_state'], axis=1)
print(dfCustomerDetail)
dfCustomerDetail.to_csv('../data_csv/CustomerDetail.csv', index= False)
