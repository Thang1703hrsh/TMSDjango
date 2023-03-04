# from .models_data import *
# import pandas as pd

# dfProductionTracking = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM production_tracking PT
#         WHERE PT.deleted_at IS NULL
#         """)

# dfProductionTracking = pd.DataFrame([item.__dict__ for item in dfProductionTracking]).drop(['_state'], axis=1)
# print(dfProductionTracking)
# dfProductionTracking.to_csv('../data_csv/ProductionTracking.csv', index= False)


# dfProductionTrackingDetail = ProductDetail.objects.raw("""  
#         SELECT *
#         FROM production_tracking_detail PTD
#         WHERE PTD.deleted_at IS NULL
#         """)

# dfProductionTrackingDetail = pd.DataFrame([item.__dict__ for item in dfProductionTrackingDetail]).drop(['_state', 'id'], axis=1)
# print(dfProductionTrackingDetail)
# dfProductionTrackingDetail.to_csv('../data_csv/ProductionTrackingDetail.csv', index= False)

