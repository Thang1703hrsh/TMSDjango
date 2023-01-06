import pandas as pd
import numpy as np



def mergeMaterialOrder(dfChild, dfParent, dfOrder):
    dfChild2 = dfChild.drop_duplicates(keep='first').reset_index(drop = True)
    dfChild2 = dfChild2.sort_values(by=['product_parent']).reset_index(drop = True)
    dfChild3 = pd.merge(dfChild2 , dfParent[['product_parent','quantity_product','temporary_quantity']], left_on='product_child', right_on='product_parent', how='inner').drop(columns = ['product_parent_y']).rename(columns = {"product_parent_x":"product_parent"})
    dfChild3 = dfChild3.reset_index(drop = True)
    g = dfChild3.groupby(["product_parent"]).cumcount().add(1)
    dfChildMerge = dfChild3.set_index(["product_parent", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
    dfChildMerge.columns = ["{}{}".format(a, b) for a, b in dfChildMerge.columns]

    dfChildMerge = dfChildMerge.reset_index()

    dfChildMerge = dfChildMerge.replace(np.nan, 0)
    dfTotalMate = pd.merge(dfParent, dfChildMerge, on='product_parent', how='left')
    dfTotalMate = dfTotalMate.replace(np.nan, 0)
    
    dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['product_child1'] == 0) & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)
    
    dfTotal = pd.merge(dfOrder , dfTotalMate, left_on='Mã vật tư', right_on='Mã vật tư Parent', how='left')
    dfTotal = dfTotal.reset_index(drop = True)
    
    dfTotalReverse = dfTotal[::-1]
    dfTotalReverse = dfTotalReverse.reset_index(drop = True)
    dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['ID_Parent']) == True].index).reset_index(drop = True)

    return dfTotalMate, dfTotalReverse
    
