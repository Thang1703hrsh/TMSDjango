from .models_data import *
import pandas as pd

dfCurrency = ProductDetail.objects.raw("""  
        SELECT *
        FROM currency 
        WHERE currency.deleted_at IS NULL
        """)

dfCurrency = pd.DataFrame([item.__dict__ for item in dfCurrency]).drop(['_state'], axis=1)
print(dfCurrency)
dfCurrency.to_csv('../data_csv/currency.csv', index= False)
