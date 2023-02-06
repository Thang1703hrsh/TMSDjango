import pandas as pd
import numpy as np
pd.options.display.max_columns = None
pd.options.mode.chained_assignment = None  # default='warn'
import time

dfChild = pd.read_csv("Child.csv")
dfParent = pd.read_csv("Parent.csv")
dfOrder = pd.read_csv("Order.csv")
dfChild
dfParent
dfOrder
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
   new_col1 = ['product_parent','code_product' , 'quantity_product' ,'temporary_quantity', 'is_outsourcing', 
      'code_product1', 'product_child1', 'quantity1',
      'quantity_product1', 'temporary_quantity1', 'code_product2',
      'product_child2', 'quantity2', 'quantity_product2',
      'temporary_quantity2', 'code_product3', 'product_child3', 'quantity3',
      'quantity_product3', 'temporary_quantity3', 'code_product4',
      'product_child4', 'quantity4', 'quantity_product4',
      'temporary_quantity4', 'code_product5', 'product_child5', 'quantity5',
      'quantity_product5', 'temporary_quantity5']
   
   dfTotalMate= dfTotalMate.reindex(columns=new_col1)
   dfTotalMate = dfTotalMate.sort_values(by= ['product_parent']).reset_index(drop = True)

   dfTotal = pd.merge(dfOrder , dfTotalMate, left_on='code_product', right_on='code_product', how='left')
   dfTotal = dfTotal.reset_index(drop = True)
   new_col2 = ['code_order' , 'position' , 'total_quota', 'quantity_out',
      'product_parent' , 'code_product' , 'quantity_product',
      'temporary_quantity', 'is_outsourcing' , 'code_product1', 'product_child1', 'quantity1',
      'quantity_product1', 'temporary_quantity1', 'code_product2',
      'product_child2', 'quantity2', 'quantity_product2',
      'temporary_quantity2', 'code_product3', 'product_child3', 'quantity3',
      'quantity_product3', 'temporary_quantity3', 'code_product4',
      'product_child4', 'quantity4', 'quantity_product4',
      'temporary_quantity4', 'code_product5', 'product_child5', 'quantity5',
      'quantity_product5', 'temporary_quantity5']
   
   dfTotal=dfTotal.reindex(columns=new_col2)

   dfTotalReverse = dfTotal[::-1]
   dfTotalReverse = dfTotalReverse.reset_index(drop = True)
   dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['product_parent']) == True].index).reset_index(drop = True)
   dfTotalReverse = dfTotalReverse[:300] 
   return dfTotalMate, dfTotalReverse
dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
dfTotalMate
ahat = dfTotalReverse.loc[0]
aMate = dfTotalMate.loc[np.where(dfTotalMate['product_parent']==ahat['product_parent'])[0][0]] ## Lấy ID từ vật tư trong ahat, suy ra ID cho aMate
dict_evaluated = {"code_order":[] , "position":[], "code_product":[] ,  "quantity" : []}

def updateDictEvaluated(dict_evaluated, aMate , string):
    dict_evaluated["quantity"].append(string)
    dict_evaluated["code_order"].append(aMate['code_order'])
    dict_evaluated["position"].append(aMate['position'])

def calLevel1(ahat, dfParent, dict_evaluated):
    sub = ahat['temporary_quantity'] - ahat['total_quota'] 
    indexCode = dfParent[dfParent['code_product'] == ahat['code_product']].index[0] 
    dfParent.at[indexCode , 'temporary_quantity'] = sub
    return sub, dfParent
listColMateTtReverse = [9,14,19,24,29] ## index cột mã vật tư theo dfTotalReverse
listColMate = [5,10,15,20,25] ## index cột mã vật tư theo dfTotalMate



def calLevel2(ahat, dfTotalMate , sub, dict_evaluated):
    dict_notenough = {"product_id": [], "index_min": [] , "arr_min": [] , "arr_sub": []}
    dict_enough = {"product_id": [], "index_min": [] , "arr_min": [], "arr_sub": []}
    count = negative = positive = 0
    aMate = dfTotalMate.loc[np.where(dfTotalMate['product_parent']==ahat['product_parent'])[0][0]] ## Lấy ID từ vật tư trong ahat, suy ra ID cho aMate
    for i in listColMate: 
        if(aMate[i] != 0):
            slSC = aMate[i+4] * aMate[i+2]
            if((slSC + sub) < 0):
                dict_notenough['product_id'].append(aMate[i+1]) 
                dict_notenough['index_min'].append(i) 
                dict_notenough['arr_min'].append(slSC) 
                dict_notenough['arr_sub'].append(slSC + sub) 
                negative = negative + 1
            else:
                dict_notenough['product_id'].append(aMate[i+1]) 
                dict_enough['index_min'].append(i) 
                dict_enough['arr_min'].append(slSC) 
                dict_notenough['arr_sub'].append(slSC + sub) 
                positive = positive + 1
            count = count + 1
        elif(aMate[5] == 0):
            return updateDictEvaluated(dict_evaluated, aMate, "not enough")
        else:
            break
    if(count == positive):
        return updateDictEvaluated(dict_evaluated, aMate, "enough")   
        
    df_notenough = pd.DataFrame(dict_notenough)
    # df_notenough.sort_values(by=['arr_min'], inplace=True)
    
    df_enough = pd.DataFrame(dict_enough)
    # df_enough.sort_values(by=['arr_min'], inplace=True)
    
    
    return aMate , df_notenough, df_enough, negative , positive
    
    
    
    
# update the quantity of material after using it
def replaceNewValue(aMate, dfParent , sub):
    count = 0
    update_sub = 0
    for i in listColMate: 
        if(aMate[i] != 0):
            indexCode = dfParent[dfParent['code_product'] == aMate[i]].index[0]
            update_sub = aMate[i+4] - sub * aMate[i+2]
            dfParent.at[indexCode , 'temporary_quantity'] = update_sub
        else:
            break
        count = count + 1
    return dfParent
# child case is primary
def checkValue(aMate , dfParent , index_min):
    indexParent = dfParent[dfParent['code_product'] == aMate[9 + (index_min * 5)]]
    if((indexParent['is_outsourcing'] == 0)):
        dict_evaluated["quantity"].append("not enough")
def checkValue(aMate , dfParent , index_min):
    for i in listColMate: 
        if(aMate[i] != 0):
            indexCode = dfParent[dfParent.index.values == aMate.name].index[0]
            if((aMate[i+2] == 0) & i == index_min):
                dict_evaluated["quantity"].append("not enough")
def recursivePrimary(ahat, dfParent, dfTotalMate):
    aMate, arr_mul, min_arr, index_min = calLevel2(ahat, dfParent, dfTotalMate)
    sublv, dfParent = replaceNewValue(aMate, dfParent, arr_mul, min_arr, index_min)
    if(min_arr + sublv):
        dict_evaluated["quantity"].append("not enough")
    else:
        indexParent = dfParent[dfParent['code_product'] == aMate[5 + (index_min * 5)]]
        if((indexParent['is_outsourcing'] == 0).bool()):
            dict_evaluated["quanlity"].append("not enough")
        else:
            recursivePrimary(ahat, dfParent, dfTotalMate)
def primary(dfTotalReverse , dfParent, dfTotalMate, index): #index là vị trí từng bộ vị từ trên xuống dưới
    ahat = dfTotalReverse.loc[index]
    if((ahat['quantity_out'] - ahat['total_quota']) >= 0.0):
        dict_evaluated["quantity"].append("enough") 
    else: 
        if(ahat['is_outsourcing'] == 0):
            sub, dfParent = calLevel1(ahat, dfParent , dict_evaluated)
            if(sub > 0):
                dict_evaluated["quantity"].append("enough")
            else:
                dict_evaluated["quantity"].append("not enough")
        else:
            sub1, dfParent = calLevel1(ahat, dfParent , dict_evaluated)
            dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild, dfParent, dfOrder)
            if(sub1 > 0):
                dict_evaluated["quantity"].append("enough")
            else:
                aMate , df_notenough, df_enough, negative , positive = calLevel2(ahat, dfTotalMate , sub, dict_evaluated)
                dfParent = replaceNewValue(aMate, dfParent , arr_mul , min_arr , index_min)
                dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
                if(min_arr + sub1 > 0):
                    dict_evaluated["quantity"].append("enough")
                else:
                    indexParent = dfParent.loc[np.where(dfParent['code_product'] == aMate[5 + (index_min * 5)])[0][0]]
                    if((indexParent['is_outsourcing'] == 0)):
                        dict_evaluated["quantity"].append("not enough")
                    else:
                        aMate , arr_mul , min_arr, index_min = calLevel2(aMate, dfParent, dfTotalMate)
                        dfParent = replaceNewValue(aMate, dfParent , arr_mul , min_arr, index_min)
                        dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
                        if(min_arr + subLv2 > 0):
                            dict_evaluated["quantity"].append("enough")
                        else:
                            indexParent = dfParent.loc[np.where(dfParent['code_product']== aMate[5 + (index_min * 5)])[0][0]]
                            if((indexParent['is_outsourcing'] == 0)):
                                dict_evaluated["quantity"].append("not enough")
                            else: 
                                aMate , arr_mul , min_arr , index_min = calLevel2(aMate, dfParent, dfTotalMate)
                                dfParent = replaceNewValue(aMate, dfParent , arr_mul , min_arr, index_min)
                                dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
                                if(min_arr + subLv3 > 0):
                                    dict_evaluated["quantity"].append("enough")
                                else:
                                    indexParent = dfParent.loc[np.where(dfParent['code_product']== aMate[5 + (index_min * 5)])[0][0]]
                                    if((indexParent['is_outsourcing'] == 0)):
                                        dict_evaluated["quantity"].append("not enough")
                                    else: 
                                        aMate , arr_mul , min_arr , index_min = calLevel2(aMate, dfParent, dfTotalMate)
                                        dfParent = replaceNewValue(aMate, dfParent , arr_mul , min_arr, index_min)
                                        dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
                                        if(min_arr + subLv4 > 0):
                                            dict_evaluated["quantity"].append("enough")
                                        else:
                                            indexParent = dfParent.loc[np.where(dfParent['code_product']== aMate[5 + (index_min * 5)])[0][0]]
                                            if((indexParent['is_outsourcing'] == 0)):
                                                dict_evaluated["quantity"].append("not enough")
                                            else:
                                                dict_evaluated["quantity"].append("not enough")

            
    dict_evaluated["code_order"].append(ahat['code_order'])
    dict_evaluated["position"].append(ahat['position'])
    return dfTotalMate, dfTotalReverse
dfParent
for i in range(0, len(dfTotalReverse)):
    dfTotalMate, dfTotalReverse = primary(dfTotalReverse ,dfParent, dfTotalMate, i)
dfEvaluted = pd.DataFrame.from_dict(dict_evaluated)
dfEvaluted
listOrder = dfEvaluted['code_order'].unique()
newDictEvalue = {"code_order": [] , "quantity": []}
for i in listOrder:
    listEva = dfEvaluted.loc[dfEvaluted['code_order'] == i]['quantity'].unique()
    if (len(listEva) == 1):
        newDictEvalue["quantity"].append(listEva[0])
        newDictEvalue["code_order"].append(i)
    else:
        if(listEva[0] != listEva[1]):
            newDictEvalue["quantity"].append("not enough")
            newDictEvalue["code_order"].append(i)
        else:
            newDictEvalue["quantity"].append(listEva)
        
dfEvalutedTt = pd.DataFrame.from_dict(newDictEvalue)
dfEvalutedTt
dfEvalutedTt.loc[dfEvalutedTt["quantity"] == "enough"]
dfEvalutedTt.loc[dfEvalutedTt["quantity"] == "not enough"]

