from .models_data import *
import pandas as pd

dfWorkingTime = ProductDetail.objects.raw("""  
        SELECT WT.id , WT.code
        FROM working_time WT
        WHERE WT.deleted_at IS NULL
        """)

dfWorkingTime = pd.DataFrame([item.__dict__ for item in dfWorkingTime]).drop(['_state'], axis=1)
print(dfWorkingTime)
dfWorkingTime.to_csv('../data_csv/WorkingTime.csv', index= False)

