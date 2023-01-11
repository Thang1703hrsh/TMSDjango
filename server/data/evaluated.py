# import pandas as pd
# import numpy as np
# pd.options.display.max_columns = None
# pd.options.mode.chained_assignment = None  # default='warn'
# import time
# from readdata import *

# # dfChild = pd.read_csv("Child.csv")
# # dfParent = pd.read_csv("Parent.csv")
# # dfOrder = pd.read_csv("Order.csv")

# dfChild =  readdfChild
# dfParent = readdfParent
# dfOrder = readdfOrder

# dfOrder_drop_dup = dfOrder.drop_duplicates(subset=['code_order', 'code_product'], keep='first').reset_index(drop= True)
# dfOrder_groupby_sum = dfOrder.groupby(['code_order', 'code_product'], as_index=False)['quantity_out'].sum()
# dfOrder_groupby_sum.sort_values(by = ['quantity_out'])
# dfOrder = pd.merge(dfOrder_drop_dup , dfOrder_groupby_sum, on=['code_order', 'code_product'], 
#                    how='inner').drop(columns = ['quantity_out_x']).rename(columns = {"quantity_out_y":"quantity_out"})


# def mergeMaterialOrder(dfChild, dfParent, dfOrder):
#    dfChild2 = dfChild.drop_duplicates(keep='first').reset_index(drop = True)
#    dfChild2 = dfChild2.sort_values(by=['product_parent']).reset_index(drop = True)
#    dfChild3 = pd.merge(dfChild2 , dfParent[['product_parent','quantity_product','temporary_quantity']], 
#                        left_on='product_child', right_on='product_parent', how='inner').drop(columns = ['product_parent_y']).rename(columns = 
#                                                                                                     {"product_parent_x":"product_parent"})
                       
#    dfChild3 = dfChild3.reset_index(drop = True)
#    g = dfChild3.groupby(["product_parent"]).cumcount().add(1)
#    dfChildMerge = dfChild3.set_index(["product_parent", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
#    dfChildMerge.columns = ["{}{}".format(a, b) for a, b in dfChildMerge.columns]

#    dfChildMerge = dfChildMerge.reset_index()

#    dfChildMerge = dfChildMerge.replace(np.nan, 0)
#    dfTotalMate = pd.merge(dfParent, dfChildMerge, on='product_parent', how='left')
#    dfTotalMate = dfTotalMate.replace(np.nan, 0)
   
#    dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['product_child1'] == 0) 
#                                               & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)
#    new_col1 = ['product_parent','code_product' , 'quantity_product' ,'temporary_quantity', 'is_outsourcing', 
#       'code_product1', 'product_child1', 'quantity1',
#       'quantity_product1', 'temporary_quantity1', 'code_product2',
#       'product_child2', 'quantity2', 'quantity_product2',
#       'temporary_quantity2', 'code_product3', 'product_child3', 'quantity3',
#       'quantity_product3', 'temporary_quantity3', 'code_product4',
#       'product_child4', 'quantity4', 'quantity_product4',
#       'temporary_quantity4', 'code_product5', 'product_child5', 'quantity5',
#       'quantity_product5', 'temporary_quantity5']
   
#    dfTotalMate= dfTotalMate.reindex(columns=new_col1)
#    dfTotalMate = dfTotalMate.sort_values(by= ['product_parent']).reset_index(drop = True)

#    dfTotal = pd.merge(dfOrder , dfTotalMate, left_on='code_product', right_on='code_product', how='left')
#    dfTotal = dfTotal.reset_index(drop = True)
#    new_col2 = ['code_order' , 'position' , 'total_quota', 'quantity_out',
#       'product_parent' , 'code_product' , 'quantity_product',
#       'temporary_quantity', 'is_outsourcing' , 'code_product1', 'product_child1', 'quantity1',
#       'quantity_product1', 'temporary_quantity1', 'code_product2',
#       'product_child2', 'quantity2', 'quantity_product2',
#       'temporary_quantity2', 'code_product3', 'product_child3', 'quantity3',
#       'quantity_product3', 'temporary_quantity3', 'code_product4',
#       'product_child4', 'quantity4', 'quantity_product4',
#       'temporary_quantity4', 'code_product5', 'product_child5', 'quantity5',
#       'quantity_product5', 'temporary_quantity5']
   
#    dfTotal=dfTotal.reindex(columns=new_col2)

#    dfTotal = dfTotal[:1000] 
#    dfTotalReverse = dfTotal[::-1]
#    dfTotalReverse = dfTotalReverse.reset_index(drop = True)
#    dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['product_parent']) 
#                                                        == True].index).reset_index(drop = True)
#    return dfTotalMate, dfTotalReverse

# dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)

# # Dictionary create output evaluated order
# dict_evaluated = {"code_order":[] , "position":[], "code_product":[] ,  "comment" : [] ,"total_quota": [] ,
#                   "temporary_quantity" : [] , "lack_of_material" : [] ,  "quantity" : [] , "lack_of_quantity": [], "is_outsourcing" : []}
# listColMateTtReverse = [9,14,19,24,29]
# listColMate = [5,10,15,20,25] 

# # append values to dictionary
# def updateDictEvaluated(dict_evaluated, aMate , string, total_quota, 
#                         temporary_quantity, lack_of_material, quantity , lack_of_quantity , is_outsourcing):
    
#     dict_evaluated["code_order"].append(aMate['code_order'])
#     dict_evaluated["position"].append(aMate['position'])
#     dict_evaluated["code_product"].append(aMate['code_product'])
#     dict_evaluated["comment"].append(string)
#     dict_evaluated["total_quota"].append(total_quota)
#     dict_evaluated["temporary_quantity"].append(temporary_quantity)
#     dict_evaluated["lack_of_material"].append(lack_of_material)
#     dict_evaluated["quantity"].append(quantity)
#     dict_evaluated["lack_of_quantity"].append(lack_of_quantity)
#     dict_evaluated["is_outsourcing"].append(is_outsourcing)
    
# # Use position calculate value in order
# def calLevel1(ahat, dfParent):
#     sub = ahat['temporary_quantity'] - ahat['total_quota'] 
#     indexCode = dfParent[dfParent['code_product'] == ahat['code_product']].index[0] 
#     dfParent.at[indexCode , 'temporary_quantity'] = sub
#     sub = np.round(sub, 2)
#     return sub, dfParent


# # update the quantity of material after using it
# def replaceNewValue(aMate, dfParent , sub):
#     update_sub = 0
#     for i in listColMate: 
#         if(aMate[i] != 0):
#             indexCode = dfParent[dfParent['code_product'] == aMate[i]].index[0]
#             update_sub = aMate[i+4] + (sub / aMate[i+2])
#             dfParent.at[indexCode , 'temporary_quantity'] = round(update_sub,2)
#         else:
#             break
#     return dfParent

# # Use child calculate value in order by recursive
# def calLevel2(ahat , product_id, dfTotalMate , sub1 , sub , dict_evaluated, dfParent, dfTotalReverse , quantity):
#     dict_notenough = {"product_id": [], "index_min": [] , "quantity": [] ,"quantity_product": [] , "temp_quantity": []}
#     count = negative = positive = 0
#     aMate = dfTotalMate.loc[np.where(dfTotalMate['product_parent'] == product_id)[0][0]] 
#     for i in listColMate: 
#         if (aMate[5] == 0):
#             return updateDictEvaluated(dict_evaluated, ahat, "not enough", ahat['total_quota'] ,sub1, aMate[i-4], quantity , sub , 0)
            
#         elif(aMate[i] != 0):
#             slSC = aMate[i+4] * aMate[i+2]
#             if((slSC + sub1) < 0):
#                 dict_notenough['product_id'].append(aMate[i+1]) 
#                 dict_notenough['index_min'].append(i) 
#                 dict_notenough['quantity'].append(quantity * aMate[i+2]) 
#                 dict_notenough['quantity_product'].append(slSC) 
#                 dict_notenough['temp_quantity'].append(np.round((slSC + sub1)/aMate[i+2] , 2)) 
#                 negative = negative + 1
#             else:
#                 positive = positive + 1
#             count = count + 1
#         else:
#             break
                
#     df_notenough = pd.DataFrame(dict_notenough)
        
#     dfParent = replaceNewValue(aMate, dfParent , sub)
#     dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
    
#     if(count == positive):
#         return updateDictEvaluated(dict_evaluated, ahat, "enough", ahat['total_quota'] , sub1, np.NaN, quantity , np.NaN, np.NaN)    
#     else:    
#         for i in range(0, negative):
#             return calLevel2(ahat, df_notenough.loc[i]['product_id'], dfTotalMate , sub1, 
#                              df_notenough.loc[i]['temp_quantity'], dict_evaluated, dfParent, 
#                              dfTotalReverse, df_notenough.loc[i]['quantity'])
        
# # function run
# def primary(dfTotalReverse , dfParent, dfTotalMate, index):
#     ahat = dfTotalReverse.loc[index]
#     if((ahat['quantity_out'] - ahat['total_quota']) >= 0.0):
#         updateDictEvaluated(dict_evaluated, ahat, "exported", ahat['total_quota'] , np.NAN, np.NAN , np.NAN , np.NAN, np.NAN)
#     else: 
#         if(ahat['is_outsourcing'] == 0):
#             sub, dfParent = calLevel1(ahat, dfParent)
#             dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
#             if(sub > 0):
#                 updateDictEvaluated(dict_evaluated, ahat, "enough", ahat['total_quota'] , sub, np.NAN, np.NAN, np.NAN , 0)
#             else:
#                 updateDictEvaluated(dict_evaluated, ahat, "not enough", ahat['total_quota'] , sub , ahat["code_product"],np.NAN, sub , 0)
#         else:
#             sub1, dfParent = calLevel1(ahat, dfParent)
#             sub = np.NAN
#             dfTotalMate,dfTotalReverse = mergeMaterialOrder(dfChild , dfParent, dfOrder)
#             if(sub1 > 0):
#                 updateDictEvaluated(dict_evaluated, ahat, "enough", ahat['total_quota'] , sub1 , np.NAN,  np.NAN, np.NAN , 1)
#             else:
#                 calLevel2(ahat , ahat['product_parent'], dfTotalMate , sub1 , sub , dict_evaluated, dfParent, dfTotalReverse , 1)
#     return dfTotalMate, dfTotalReverse
            
# for i in range(0, len(dfTotalReverse)):
#     dfTotalMate, dfTotalReverse = primary(dfTotalReverse ,dfParent, dfTotalMate, i)
    
    
# dfEvaluted = pd.DataFrame.from_dict(dict_evaluated)
# # dfEvaluted = dfEvaluted[::-1].reset_index(drop = True)

# # output data to file xlsx
# dfEvaluted.to_excel('data.xlsx')


# listOrder = dfEvaluted['code_order'].unique()
# newDictEvalue = {"code_order": [] , "quantity": []}
# for i in listOrder:
#     listEva = dfEvaluted.loc[dfEvaluted['code_order'] == i]['quantity'].unique()
#     if (len(listEva) == 1):
#         newDictEvalue["quantity"].append(listEva[0])
#         newDictEvalue["code_order"].append(i)
#     else:
#         if(listEva[0] != listEva[1]):
#             newDictEvalue["quantity"].append("not enough")
#             newDictEvalue["code_order"].append(i)
#         else:
#             newDictEvalue["quantity"].append(listEva)
        
# dfEvalutedTt = pd.DataFrame.from_dict(newDictEvalue)



