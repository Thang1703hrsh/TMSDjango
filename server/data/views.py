from django.shortcuts import render
# from .models import Orders,OrderQuota, OrderBooking, OrderDetail
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import timeit

from django.db import connection
from django.core.cache import cache 
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from .serializers import *
import pandas as pd
from django_pandas.io import read_frame
import numpy as np
import itertools
import json
    
    
def get_nodes(links , node):
    d = {}
    d['name'] = node[0]
    d['title'] = node[1]
    d['quantity'] = node[2]
    children = get_children(links, node)
    if children:
        d['children'] = [get_nodes(links , child) for child in children]
    return d

def get_children(links , node):
    return [(x[3],x[4],x[5]) for x in links if x[0] == node[0]]

class OutsourcingProductMaterialsAPIView(APIView):
        model = OutsourcingProductMaterials
        model = ProductDetail
        def get(self, request):
                OutProdMate = OutsourcingProductMaterials.objects.filter(deleted_at__isnull = True).order_by('outsourcing_product_id').values_list('outsourcing_product_id' , 'product_id')
                dfOutProdMate = pd.DataFrame(OutProdMate , columns= ['outsourcing_product_id' , 'product_id'])
                proDetail = ProductDetail.objects.filter(deleted_at__isnull = True).order_by('product_id').values_list('code' , 'name' , 'product_id' , 'quantity')
                dfproDetail = pd.DataFrame(proDetail , columns= ['code' , 'name' , 'product_id' , 'quantity'])
                
                # print(len(dfOutProdMate['outsourcing_product_id'].drop_duplicates().reset_index(drop= True)))
                dfOutProdMate = dfOutProdMate.merge(dfproDetail[['product_id' , 'code' , 'name', 'quantity']] , on = 'product_id', how = 'left')
                dfOutProdMate = dfOutProdMate.rename(columns= {"code" : "child_code" , "product_id" : "child_id" , "outsourcing_product_id" : "parent_id" , 'name' : 'child_name' , 'quantity': 'child_quantity'})
                
                dfproDetail = dfproDetail.rename(columns= {"code" : "parent_code" , "product_id" : "parent_id" , 'quantity': 'parent_quantity' } )
                
                dfOutProdMate = dfOutProdMate.merge(dfproDetail[['parent_id' , 'parent_code' , 'name' , 'parent_quantity']] , on = 'parent_id', how = 'left')
                dfOutProdMate = dfOutProdMate.dropna().reset_index(drop = True)
                dfOutProdMate[dfOutProdMate['parent_code'].isna()]
                
                
                links = []
                for i in range(0 , dfOutProdMate.shape[0]):
                        a = dfOutProdMate.loc[i]
                        links.append((a['parent_code'] , a['name'] , a['parent_quantity'] ,a['child_code'] , a['child_name'] , a['child_quantity']))
                        
                parents, pr_name , parent_quantity, children, child_name, child_quantity = zip(*links)
                parents = list(zip(parents , pr_name, parent_quantity))
                children = list(zip(children , child_name, child_quantity))
                root_nodes = {x for x in parents if x not in children}

                for node in root_nodes:
                        links.append(('Root', '' , '' , node[0] , node[1] , node[2]))
                tree = get_nodes(links , ('Root' , '' , ''))
                
                # tree2 = {"total product": len(dfproDetail) , "total product is parent" : len(dfOutProdMate['parent_id'].drop_duplicates().reset_index(drop= True)),
                #          "total product is child" : len(dfproDetail) - len(dfOutProdMate['parent_id'].drop_duplicates().reset_index(drop= True)),
                #          }
                # tree2.update(tree)
                
                return Response(tree)
        
def get_nodes1(links , node):
    d = {}
    d['name'] = node[0]
    d['title'] = node[1]
    children = get_children1(links, node)
    if children:
        d['children'] = [get_nodes1(links , child) for child in children]
    return d

def get_children1(links , node):
    return [(x[2],x[3]) for x in links if x[0] == node[0]]

       
class OutsourcingProductAPIView(APIView):
        model = OutsourcingProductMaterials
        model = ProductDetail
        def get(self, request):
                OutProdMate = OutsourcingProductMaterials.objects.filter(deleted_at__isnull = True).order_by('outsourcing_product_id').values_list('outsourcing_product_id' , 'product_id')
                dfOutProdMate = pd.DataFrame(OutProdMate , columns= ['outsourcing_product_id' , 'product_id'])
                proDetail = ProductDetail.objects.filter(deleted_at__isnull = True).order_by('product_id').values_list('code' , 'name' , 'product_id')
                dfproDetail = pd.DataFrame(proDetail , columns= ['code' , 'name' , 'product_id'])

                dfOutProdMate = dfOutProdMate.merge(dfproDetail[['product_id' , 'code' , 'name']] , on = 'product_id', how = 'left')
                dfOutProdMate = dfOutProdMate.rename(columns= {"code" : "child_code" , "product_id" : "child_id" , "outsourcing_product_id" : "parent_id" , 'name' : 'child_name'})
                dfproDetail = dfproDetail.rename(columns= {"code" : "parent_code" , "product_id" : "parent_id" } )
                
                dfOutProdMate = dfOutProdMate.merge(dfproDetail[['parent_id' , 'parent_code' , 'name']] , on = 'parent_id', how = 'left')
                dfOutProdMate = dfOutProdMate.dropna().reset_index(drop = True)
                dfOutProdMate[dfOutProdMate['parent_code'].isna()]
                
                dfOutProdMate = dfOutProdMate.rename(columns= {"parent_id" : "child_id" , "child_id" : "parent_id" , "parent_code" : "child_code" , "child_code" : "parent_code" , "name" : "child_name",
                                                               "child_name": "name"})
                
                links = []
                for i in range(0 , dfOutProdMate.shape[0]):
                        a = dfOutProdMate.loc[i]
                        links.append((a['parent_code'] , a['name'] ,a['child_code'] , a['child_name']))
                parents, pr_name , children, child_name  = zip(*links)
                parents = list(zip(parents , pr_name))
                children = list(zip(children , child_name))
                root_nodes = {x for x in parents if x not in children}

                for node in root_nodes:
                        links.append(('Root', '' , node[0] , node[1]))
                tree = get_nodes1(links , ('Root' , ''))
                tree2 = {"total product": len(dfproDetail) , "total product is parent" : len(dfOutProdMate['parent_id'].drop_duplicates().reset_index(drop= True)),
                         "total product is child" : len(dfproDetail) - len(dfOutProdMate['parent_id'].drop_duplicates().reset_index(drop= True)),
                         }
                tree2.update(tree)
                
                return Response(tree2)

class OrderAPIView(APIView):
        model = OrderDetail
        def get(self, request):
                queryset = OrderDetail.objects.raw(""" 
                        SELECT OQ.id, OQ.order_id, OQ.product_id, PD.code AS product_code, OS.status AS order_status,OQ.position ,OQ.total_quota, OD.is_complete AS complete_order, OBS.status AS booking_status
                                FROM order_quota AS OQ JOIN product_detail PD ON OQ.product_id = PD.product_id
                                        JOIN order_status AS OS ON OS.order_id = OQ.order_id
                                        JOIN orders ON orders.id = OQ.order_id
                                        JOIN order_booking AS OB ON OB.order_id = OQ.order_id
                                        JOIN order_detail AS OD ON OD.order_id = OQ.order_id
                                        JOIN order_booking_status AS OBS ON OBS.order_booking_id = OQ.order_booking_id

                                WHERE OQ.deleted_at IS NULL AND PD.deleted_at IS NULL AND OS.deleted_at IS NULL AND orders.deleted_at IS NULL
                                        AND OB.deleted_at IS NULL AND OD.deleted_at IS NULL AND OBS.deleted_at IS NULL
                
                                ORDER BY OS.order_id ASC
                        """)[0:20]
                
                mydata = orderDetailSerializer(queryset, many = True)
                return Response(mydata.data)

# dfOrder = ProductDetail.objects.raw("""  
#         SELECT 1 id, OQ.order_id, OQ.product_id, PD.code AS product_code, OS.status AS order_status,OQ.position ,OQ.total_quota, OD.is_complete AS complete_order, OBS.status AS booking_status
#                 FROM order_quota AS OQ JOIN product_detail PD ON OQ.product_id = PD.product_id
#                         JOIN order_status AS OS ON OS.order_id = OQ.order_id
#                         JOIN orders ON orders.id = OQ.order_id
#                         JOIN order_booking AS OB ON OB.order_id = OQ.order_id
#                         JOIN order_detail AS OD ON OD.order_id = OQ.order_id
#                         JOIN order_booking_status AS OBS ON OBS.order_booking_id = OQ.order_booking_id

#                 WHERE OQ.deleted_at IS NULL AND PD.deleted_at IS NULL AND OS.deleted_at IS NULL AND orders.deleted_at IS NULL
#                         AND OB.deleted_at IS NULL AND OD.deleted_at IS NULL AND OBS.deleted_at IS NULL

#                 ORDER BY OS.order_id ASC;""")
# dfOrder = pd.DataFrame([item.__dict__ for item in dfOrder]).drop(['_state', 'id'], axis=1)

# dfProduct = ProductDetail.objects.raw("""  
#         SELECT 1 id, PD.product_id , PD.code as product_code , PD.quantity AS quantity_product , PD.is_outsourcing
#         FROM product_detail PD  WHERE PD.deleted_at IS NULL 
#                 AND PD.in_trash != 1
#         ORDER BY PD.product_id ASC """)
# dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)

# dfRelationship = ProductDetail.objects.raw("""  
#         SELECT 1 id, OPM.outsourcing_product_id, OPM.product_id , PD.code as product_code , OPM.quantity as quota_outsourcing
#         FROM outsourcing_product_materials AS OPM JOIN product_detail AS PD 
#                                         ON OPM.product_id = PD.product_id 
#         WHERE OPM.deleted_at IS NULL 
#                 AND PD.deleted_at IS NULL """)

# dfRelationship = pd.DataFrame([item.__dict__ for item in dfRelationship]).drop(['_state', 'id'], axis=1)


# def mergeMaterialOrder(dfRelationship, dfProduct, dfOrder):
#         dfOrder = dfOrder.rename(columns = {"product_id":"parent_product"})
#         dfRelationship = dfRelationship.rename(columns = {"product_id":"child_product" , 'outsourcing_product_id' : 'parent_product'})
#         colProduct = ['product_id', 'product_code' , 'quantity_product' , 'is_outsourcing']
#         dfProduct = dfProduct.reindex(columns=colProduct).rename(columns = {"product_id":"parent_product"})

#         dfRelationship_dropdup = dfRelationship.drop_duplicates(keep='first').reset_index(drop = True).sort_values(by=['parent_product']).reset_index(drop = True)
#         dfRelationship_merge = pd.merge(dfRelationship_dropdup , dfProduct[['parent_product','quantity_product']], left_on='child_product', right_on='parent_product', how='inner').drop(columns = ['parent_product_y']).rename(columns = {"parent_product_x":"parent_product"})
#         dfRelationship_merge = dfRelationship_merge.reset_index(drop = True)
#         g = dfRelationship_merge.groupby(["parent_product"]).cumcount().add(1)
#         dfRelationshipMerge = dfRelationship_merge.set_index(["parent_product", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
#         dfRelationshipMerge.columns = ["{}{}".format(a, b) for a, b in dfRelationshipMerge.columns]

#         dfRelationshipMerge = dfRelationshipMerge.reset_index()

#         dfRelationshipMerge = dfRelationshipMerge.replace(np.nan, 0)
#         dfTotalMate = pd.merge(dfProduct, dfRelationshipMerge, on='parent_product', how='left')
#         dfTotalMate = dfTotalMate.replace(np.nan, 0)

#         dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['child_product1'] == 0) & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)

#         dfTotalMate = dfTotalMate.sort_values(by= ['parent_product']).reset_index(drop = True) 
#         dfTotal = pd.merge(dfOrder , dfTotalMate, on=['product_code', 'parent_product'], how='left')

#         dfTotal = dfTotal[:100] 
#         dfTotalReverse = dfTotal[::-1]
#         dfTotalReverse = dfTotalReverse.reset_index(drop = True)
#         dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['parent_product']) == True].index).reset_index(drop = True)
#         dfTotalReverse
#         return dfTotalMate, dfTotalReverse

# dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfRelationship , dfProduct, dfOrder)


# dict = {"parent_product": [] ,"child_product" : [],"quota_outsourcing" : [] , "level" : [] , 'size_level_next': []}

# def appendDict(dict, parent_product , child_product, quota_outsourcing, level, size_level_next):
#         dict["parent_product"].append(parent_product)
#         dict["child_product"].append(child_product)
#         dict["quota_outsourcing"].append(quota_outsourcing)
#         dict["level"].append(level)
#         dict["size_level_next"].append(size_level_next)


# # calculate the quantity of primary materials of secondary materials
# def cal_size_level_next(aMate):
#         size_level = 0
#         for i in range(1, 6):
#                 if (aMate['child_product{}'.format(i)] != 0):
#                         size_level = size_level + 1
#         return size_level

# # recursive calculator number need with child is primary, not secondary
# def recursivelyNumberNeed(dict, dfTotalMate, parent_product ,product_id, quota, level, size_level_next):
#         aMate = dfTotalMate.loc[np.where(dfTotalMate['parent_product'] == product_id)[0][0]] 
#         if ((aMate['is_outsourcing'] == 0) & (size_level_next == 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0) 
#         elif ((aMate['is_outsourcing'] == 0) & (size_level_next != 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0)
#         elif((aMate['is_outsourcing'] != 0) & (size_level_next != 0)): 
#                 size_level_next = cal_size_level_next(aMate) 
#                 for i in range(1, size_level_next + 1):
#                         dict["quota_outsourcing"].append(quota)
#                         level = level - (i - 1)
#                         dict["level"].append(level)
#                         dict["size_level_next"].append(size_level_next)
#                         quota = quota * aMate['quota_outsourcing{}'.format(i)]
#                         level = level + 1
#                         dict["parent_product"].append(parent_product)
#                         child_product = aMate['child_product{}'.format(i)]
#                         dict["child_product"].append(product_id)
#                         recursivelyNumberNeed(dict, dfTotalMate, parent_product, child_product, quota, level, size_level_next)
                
                
# def recursivelyCalculateSecondaryNeed(dfTotalMate):
#         for i in range(0 , len(dfTotalMate)):
#                 aMaterial = dfTotalMate.loc[i]
#                 parent_product = aMaterial['parent_product']
#                 size_level_next = cal_size_level_next(aMaterial)
#                 if (size_level_next == 0): 
#                         level = 1
#                         appendDict(dict, parent_product , 0, 0, level, 0)
#                 else:
#                         for i in range(1 , size_level_next + 1):
#                                 quota = 1
#                                 level = 2
#                                 quota = quota * aMaterial['quota_outsourcing{}'.format(i)]
#                                 product_id = aMaterial['child_product{}'.format(i)]
#                                 # appendDict(dict, parent_product , child_product, quota, level, size_level_next) 
#                                 recursivelyNumberNeed(dict, dfTotalMate, parent_product, product_id, quota, level, size_level_next)
                                
#         return dict

# dict = recursivelyCalculateSecondaryNeed(dfTotalMate)
# multiLevelBOMOrder = pd.DataFrame.from_dict(dict)
# print(multiLevelBOMOrder)