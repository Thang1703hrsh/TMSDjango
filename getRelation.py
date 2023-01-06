import numpy as np
import pandas as pd  
import time


dfOrder = pd.read_csv("data_csv/Order.csv")
dfProduct = pd.read_csv("data_csv/Product.csv")
dfRelationship = pd.read_csv("data_csv/Relationship.csv")


def mergeMaterialOrder(dfRelationship, dfProduct, dfOrder):
   dfOrder = dfOrder.rename(columns = {"product_id":"parent_product"})
   dfRelationship = dfRelationship.rename(columns = {"product_id":"child_product" , 'outsourcing_product_id' : 'parent_product'})
   colProduct = ['product_id', 'product_code' , 'quantity_product' , 'is_outsourcing']
   dfProduct = dfProduct.reindex(columns=colProduct).rename(columns = {"product_id":"parent_product"})

   dfRelationship_dropdup = dfRelationship.drop_duplicates(keep='first').reset_index(drop = True).sort_values(by=['parent_product']).reset_index(drop = True)
   dfRelationship_merge = pd.merge(dfRelationship_dropdup , dfProduct[['parent_product','quantity_product']], left_on='child_product', right_on='parent_product', how='inner').drop(columns = ['parent_product_y']).rename(columns = {"parent_product_x":"parent_product"})
   dfRelationship_merge = dfRelationship_merge.reset_index(drop = True)
   g = dfRelationship_merge.groupby(["parent_product"]).cumcount().add(1)
   dfRelationshipMerge = dfRelationship_merge.set_index(["parent_product", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
   dfRelationshipMerge.columns = ["{}{}".format(a, b) for a, b in dfRelationshipMerge.columns]

   dfRelationshipMerge = dfRelationshipMerge.reset_index()

   dfRelationshipMerge = dfRelationshipMerge.replace(np.nan, 0)
   dfTotalMate = pd.merge(dfProduct, dfRelationshipMerge, on='parent_product', how='left')
   dfTotalMate = dfTotalMate.replace(np.nan, 0)

   dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['child_product1'] == 0) & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)

   dfTotalMate = dfTotalMate.sort_values(by= ['parent_product']).reset_index(drop = True) 
   dfTotal = pd.merge(dfOrder , dfTotalMate, on=['product_code', 'parent_product'], how='left')

   # dfTotal = dfTotal[:1000] 
   dfTotalReverse = dfTotal[::-1]
   dfTotalReverse = dfTotalReverse.reset_index(drop = True)
   dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['parent_product']) == True].index).reset_index(drop = True)
   dfTotalReverse
   return dfTotalMate, dfTotalReverse

dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfRelationship , dfProduct, dfOrder)


dict = {"parent_product": [] ,"child_product" : [],"quota_outsourcing" : [] , "level" : [] , 'size_level_next': []}

def appendDict(dict, parent_product , child_product, quota_outsourcing, level, size_level_next):
    dict["parent_product"].append(parent_product)
    dict["child_product"].append(child_product)
    dict["quota_outsourcing"].append(quota_outsourcing)
    dict["level"].append(level)
    dict["size_level_next"].append(size_level_next)
    

# calculate the quantity of primary materials of secondary materials
def cal_size_level_next(aMate):
    size_level = 0
    for i in range(1, 6):
        if (aMate['child_product{}'.format(i)] != 0):
            size_level = size_level + 1
    return size_level

# recursive calculator number need with child is primary, not secondary
def recursivelyNumberNeed(dict, dfTotalMate, parent_product ,product_id, quota, level, size_level_next):
    aMate = dfTotalMate.loc[np.where(dfTotalMate['parent_product'] == product_id)[0][0]] 
    if ((aMate['is_outsourcing'] == 0) & (size_level_next == 0)): 
        appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0) 
    elif ((aMate['is_outsourcing'] == 0) & (size_level_next != 0)): 
        appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0)
        # if(size_level_next >= 2):
        #     level = level - 1
    elif((aMate['is_outsourcing'] != 0) & (size_level_next != 0)): 
        size_level_next = cal_size_level_next(aMate) 
        for i in range(1, size_level_next + 1):
            dict["quota_outsourcing"].append(quota)
            level = level - (i - 1)
            dict["level"].append(level)
            dict["size_level_next"].append(size_level_next)
            quota = quota * aMate['quota_outsourcing{}'.format(i)]
            level = level + 1
            dict["parent_product"].append(parent_product)
            child_product = aMate['child_product{}'.format(i)]
            dict["child_product"].append(product_id)
            recursivelyNumberNeed(dict, dfTotalMate, parent_product, child_product, quota, level, size_level_next)
            
            
            
# appendDict(dict, material_order , child_product, quota_outsourcing, level, size_level_next):
# recursive calculator secondary need
def recursivelyCalculateSecondaryNeed(dfTotalMate):
    for i in range(0 , len(dfTotalMate)):
        aMaterial = dfTotalMate.loc[i]
        parent_product = aMaterial['parent_product']
        size_level_next = cal_size_level_next(aMaterial)
        if (size_level_next == 0): 
            level = 1
            appendDict(dict, parent_product , 0, 0, level, 0)
        else:
            for i in range(1 , size_level_next + 1):
                quota = 1
                level = 2
                quota = quota * aMaterial['quota_outsourcing{}'.format(i)]
                product_id = aMaterial['child_product{}'.format(i)]
                # appendDict(dict, parent_product , child_product, quota, level, size_level_next) 
                recursivelyNumberNeed(dict, dfTotalMate, parent_product, product_id, quota, level, size_level_next)
                        
    return dict
            
dict = recursivelyCalculateSecondaryNeed(dfTotalMate)
multiLevelBOMOrder = pd.DataFrame.from_dict(dict)
print(multiLevelBOMOrder)



