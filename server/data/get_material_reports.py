# from .models import *
# import pandas as pd


# ## Outsourcing Stock In Detail
# dfMaterialReports = ProductDetail.objects.raw("""  
#         SELECT 1 id, MR.*
#             FROM ttd_staging_report.material_reports MR
#             WHERE MR.deleted_at IS NULL  
#             ORDER BY `MR`.`product_id` ASC;
#         """)

# dfMaterialReports = pd.DataFrame([item.__dict__ for item in dfMaterialReports]).drop(['_state', 'id'], axis=1)
# print(dfMaterialReports)
# dfMaterialReports.to_csv('data_csv/MaterialReports.csv', index= False)

