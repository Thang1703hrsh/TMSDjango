from django.shortcuts import render
# from .models import Orders,OrderQuota, OrderBooking, OrderDetail
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.db import connection
from django.core.cache import cache 
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from .serializers import *
import pandas as pd
from django_pandas.io import read_frame


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


# class getRalationship(APIView):
#         model = ProductDetail
#         def get(self, request):
#                 getOrder = ProductDetail.objects.raw("""  
#                         SELECT 1 id, OQ.order_id, OQ.product_id, PD.code AS product_code, OS.status AS order_status,OQ.position ,OQ.total_quota, OD.is_complete AS complete_order, OBS.status AS booking_status
#                                 FROM order_quota AS OQ JOIN product_detail PD ON OQ.product_id = PD.product_id
#                                         JOIN order_status AS OS ON OS.order_id = OQ.order_id
#                                         JOIN orders ON orders.id = OQ.order_id
#                                         JOIN order_booking AS OB ON OB.order_id = OQ.order_id
#                                         JOIN order_detail AS OD ON OD.order_id = OQ.order_id
#                                         JOIN order_booking_status AS OBSON OBS.order_booking_id = OQ.order_booking_id

#                                 WHERE OQ.deleted_at IS NULL AND PD.deleted_at IS NULL AND OS.deleted_at IS NULL AND orders.deleted_at IS NULL
#                                         AND OB.deleted_at IS NULL AND OD.deleted_at IS NULL AND OBS.deleted_at IS NULL
                
#                                 ORDER BY OS.order_id ASC;""")
#                 getOrder = pd.DataFrame([item.__dict__ for item in getOrder]).drop(['_state', 'id'], axis=1)
                
#                 dfProduct = ProductDetail.objects.raw("""  
#                         SELECT 1 id, PD.product_id , PD.code as product_code , PD.quantity AS quantity_product , PD.is_outsourcing
#                         FROM product_detail PD  WHERE PD.deleted_at IS NULL 
#                                 AND PD.in_trash != 1
#                         ORDER BY PD.product_id ASC """)
#                 dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)
                
#                 dfRelationship = ProductDetail.objects.raw("""  
#                         SELECT 1 id, OPM.outsourcing_product_id, OPM.product_id , PD.code as product_code , OPM.quantity as quota_outsourcing
#                         FROM outsourcing_product_materials AS OPM JOIN product_detail AS PD 
#                                                         ON OPM.product_id = PD.product_id 
#                         WHERE OPM.deleted_at IS NULL 
#                                 AND PD.deleted_at IS NULL """)

#                 dfRelationship = pd.DataFrame([item.__dict__ for item in dfRelationship]).drop(['_state', 'id'], axis=1)

        
#         def mergeMaterialOrder(dfRelationship, dfProduct, dfOrder):
#                 dfOrder = dfOrder.rename(columns = {"product_id":"parent_product"})
#                 dfRelationship = dfRelationship.rename(columns = {"product_id":"child_product" , 'outsourcing_product_id' : 'parent_product'})
#                 colProduct = ['product_id', 'product_code' , 'quantity_product' , 'is_outsourcing']
#                 dfProduct = dfProduct.reindex(columns=colProduct).rename(columns = {"product_id":"parent_product"})

#                 dfRelationship_dropdup = dfRelationship.drop_duplicates(keep='first').reset_index(drop = True).sort_values(by=['parent_product']).reset_index(drop = True)
#                 dfRelationship_merge = pd.merge(dfRelationship_dropdup , dfProduct[['parent_product','quantity_product']], left_on='child_product', right_on='parent_product', how='inner').drop(columns = ['parent_product_y']).rename(columns = {"parent_product_x":"parent_product"})
#                 dfRelationship_merge = dfRelationship_merge.reset_index(drop = True)
#                 g = dfRelationship_merge.groupby(["parent_product"]).cumcount().add(1)
#                 dfRelationshipMerge = dfRelationship_merge.set_index(["parent_product", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
#                 dfRelationshipMerge.columns = ["{}{}".format(a, b) for a, b in dfRelationshipMerge.columns]

#                 dfRelationshipMerge = dfRelationshipMerge.reset_index()

#                 dfRelationshipMerge = dfRelationshipMerge.replace(np.nan, 0)
#                 dfTotalMate = pd.merge(dfProduct, dfRelationshipMerge, on='parent_product', how='left')
#                 dfTotalMate = dfTotalMate.replace(np.nan, 0)

#                 dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['child_product1'] == 0) & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)

#                 dfTotalMate = dfTotalMate.sort_values(by= ['parent_product']).reset_index(drop = True) 
#                 dfTotal = pd.merge(dfOrder , dfTotalMate, on=['product_code', 'parent_product'], how='left')

#                 dfTotal = dfTotal[:100] 
#                 dfTotalReverse = dfTotal[::-1]
#                 dfTotalReverse = dfTotalReverse.reset_index(drop = True)
#                 dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['parent_product']) == True].index).reset_index(drop = True)
#                 dfTotalReverse
#                 return dfTotalMate, dfTotalReverse

#         dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfRelationship , dfProduct, dfOrder)


#         dict = {"parent_product": [] ,"child_product" : [],"quota_outsourcing" : [] , "level" : [] , 'size_level_next': []}

#         def appendDict(dict, parent_product , child_product, quota_outsourcing, level, size_level_next):
#         dict["parent_product"].append(parent_product)
#         dict["child_product"].append(child_product)
#         dict["quota_outsourcing"].append(quota_outsourcing)
#         dict["level"].append(level)
#         dict["size_level_next"].append(size_level_next)
        

#         # calculate the quantity of primary materials of secondary materials
#         def cal_size_level_next(aMate):
#         size_level = 0
#         for i in range(1, 6):
#                 if (aMate['child_product{}'.format(i)] != 0):
#                 size_level = size_level + 1
#         return size_level

#         # recursive calculator number need with child is primary, not secondary
#         def recursivelyNumberNeed(dict, dfTotalMate, parent_product ,product_id, quota, level, size_level_next):
#         aMate = dfTotalMate.loc[np.where(dfTotalMate['parent_product'] == product_id)[0][0]] 
#         if ((aMate['is_outsourcing'] == 0) & (size_level_next == 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0) 
#         elif ((aMate['is_outsourcing'] == 0) & (size_level_next != 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0)
#         elif((aMate['is_outsourcing'] != 0) & (size_level_next != 0)): 
#                 size_level_next = cal_size_level_next(aMate) 
#                 for i in range(1, size_level_next + 1):
#                 dict["quota_outsourcing"].append(quota)
#                 level = level - (i - 1)
#                 dict["level"].append(level)
#                 dict["size_level_next"].append(size_level_next)
#                 quota = quota * aMate['quota_outsourcing{}'.format(i)]
#                 level = level + 1
#                 dict["parent_product"].append(parent_product)
#                 child_product = aMate['child_product{}'.format(i)]
#                 dict["child_product"].append(product_id)
#                 recursivelyNumberNeed(dict, dfTotalMate, parent_product, child_product, quota, level, size_level_next)
                
                
#         def recursivelyCalculateSecondaryNeed(dfTotalMate):
#         for i in range(0 , len(dfTotalMate)):
#                 aMaterial = dfTotalMate.loc[i]
#                 parent_product = aMaterial['parent_product']
#                 size_level_next = cal_size_level_next(aMaterial)
#                 if (size_level_next == 0): 
#                 level = 1
#                 appendDict(dict, parent_product , 0, 0, level, 0)
#                 else:
#                 for i in range(1 , size_level_next + 1):
#                         quota = 1
#                         level = 2
#                         quota = quota * aMaterial['quota_outsourcing{}'.format(i)]
#                         product_id = aMaterial['child_product{}'.format(i)]
#                         # appendDict(dict, parent_product , child_product, quota, level, size_level_next) 
#                         recursivelyNumberNeed(dict, dfTotalMate, parent_product, product_id, quota, level, size_level_next)
                                
#         return dict
# class getRalationship(APIView):
#         model = ProductDetail
#         def get(self, request):
#                 getOrder = ProductDetail.objects.raw("""  
#                         SELECT 1 id, OQ.order_id, OQ.product_id, PD.code AS product_code, OS.status AS order_status,OQ.position ,OQ.total_quota, OD.is_complete AS complete_order, OBS.status AS booking_status
#                                 FROM order_quota AS OQ JOIN product_detail PD ON OQ.product_id = PD.product_id
#                                         JOIN order_status AS OS ON OS.order_id = OQ.order_id
#                                         JOIN orders ON orders.id = OQ.order_id
#                                         JOIN order_booking AS OB ON OB.order_id = OQ.order_id
#                                         JOIN order_detail AS OD ON OD.order_id = OQ.order_id
#                                         JOIN order_booking_status AS OBSON OBS.order_booking_id = OQ.order_booking_id

#                                 WHERE OQ.deleted_at IS NULL AND PD.deleted_at IS NULL AND OS.deleted_at IS NULL AND orders.deleted_at IS NULL
#                                         AND OB.deleted_at IS NULL AND OD.deleted_at IS NULL AND OBS.deleted_at IS NULL
                
#                                 ORDER BY OS.order_id ASC;""")
#                 getOrder = pd.DataFrame([item.__dict__ for item in getOrder]).drop(['_state', 'id'], axis=1)
                
#                 dfProduct = ProductDetail.objects.raw("""  
#                         SELECT 1 id, PD.product_id , PD.code as product_code , PD.quantity AS quantity_product , PD.is_outsourcing
#                         FROM product_detail PD  WHERE PD.deleted_at IS NULL 
#                                 AND PD.in_trash != 1
#                         ORDER BY PD.product_id ASC """)
#                 dfProduct = pd.DataFrame([item.__dict__ for item in dfProduct]).drop(['_state', 'id'], axis=1)
                
#                 dfRelationship = ProductDetail.objects.raw("""  
#                         SELECT 1 id, OPM.outsourcing_product_id, OPM.product_id , PD.code as product_code , OPM.quantity as quota_outsourcing
#                         FROM outsourcing_product_materials AS OPM JOIN product_detail AS PD 
#                                                         ON OPM.product_id = PD.product_id 
#                         WHERE OPM.deleted_at IS NULL 
#                                 AND PD.deleted_at IS NULL """)

#                 dfRelationship = pd.DataFrame([item.__dict__ for item in dfRelationship]).drop(['_state', 'id'], axis=1)

        
#         def mergeMaterialOrder(dfRelationship, dfProduct, dfOrder):
#                 dfOrder = dfOrder.rename(columns = {"product_id":"parent_product"})
#                 dfRelationship = dfRelationship.rename(columns = {"product_id":"child_product" , 'outsourcing_product_id' : 'parent_product'})
#                 colProduct = ['product_id', 'product_code' , 'quantity_product' , 'is_outsourcing']
#                 dfProduct = dfProduct.reindex(columns=colProduct).rename(columns = {"product_id":"parent_product"})

#                 dfRelationship_dropdup = dfRelationship.drop_duplicates(keep='first').reset_index(drop = True).sort_values(by=['parent_product']).reset_index(drop = True)
#                 dfRelationship_merge = pd.merge(dfRelationship_dropdup , dfProduct[['parent_product','quantity_product']], left_on='child_product', right_on='parent_product', how='inner').drop(columns = ['parent_product_y']).rename(columns = {"parent_product_x":"parent_product"})
#                 dfRelationship_merge = dfRelationship_merge.reset_index(drop = True)
#                 g = dfRelationship_merge.groupby(["parent_product"]).cumcount().add(1)
#                 dfRelationshipMerge = dfRelationship_merge.set_index(["parent_product", g]).unstack(fill_value=0).sort_index(axis=1, level=1)
#                 dfRelationshipMerge.columns = ["{}{}".format(a, b) for a, b in dfRelationshipMerge.columns]

#                 dfRelationshipMerge = dfRelationshipMerge.reset_index()

#                 dfRelationshipMerge = dfRelationshipMerge.replace(np.nan, 0)
#                 dfTotalMate = pd.merge(dfProduct, dfRelationshipMerge, on='parent_product', how='left')
#                 dfTotalMate = dfTotalMate.replace(np.nan, 0)

#                 dfTotalMate = dfTotalMate.drop(dfTotalMate[(dfTotalMate['child_product1'] == 0) & (dfTotalMate['is_outsourcing'] == 1)].index).reset_index(drop = True)

#                 dfTotalMate = dfTotalMate.sort_values(by= ['parent_product']).reset_index(drop = True) 
#                 dfTotal = pd.merge(dfOrder , dfTotalMate, on=['product_code', 'parent_product'], how='left')

#                 dfTotal = dfTotal[:100] 
#                 dfTotalReverse = dfTotal[::-1]
#                 dfTotalReverse = dfTotalReverse.reset_index(drop = True)
#                 dfTotalReverse = dfTotalReverse.drop(dfTotalReverse[np.isnan(dfTotalReverse['parent_product']) == True].index).reset_index(drop = True)
#                 dfTotalReverse
#                 return dfTotalMate, dfTotalReverse

#         dfTotalMate, dfTotalReverse = mergeMaterialOrder(dfRelationship , dfProduct, dfOrder)


#         dict = {"parent_product": [] ,"child_product" : [],"quota_outsourcing" : [] , "level" : [] , 'size_level_next': []}

#         def appendDict(dict, parent_product , child_product, quota_outsourcing, level, size_level_next):
#         dict["parent_product"].append(parent_product)
#         dict["child_product"].append(child_product)
#         dict["quota_outsourcing"].append(quota_outsourcing)
#         dict["level"].append(level)
#         dict["size_level_next"].append(size_level_next)
        

#         # calculate the quantity of primary materials of secondary materials
#         def cal_size_level_next(aMate):
#         size_level = 0
#         for i in range(1, 6):
#                 if (aMate['child_product{}'.format(i)] != 0):
#                 size_level = size_level + 1
#         return size_level

#         # recursive calculator number need with child is primary, not secondary
#         def recursivelyNumberNeed(dict, dfTotalMate, parent_product ,product_id, quota, level, size_level_next):
#         aMate = dfTotalMate.loc[np.where(dfTotalMate['parent_product'] == product_id)[0][0]] 
#         if ((aMate['is_outsourcing'] == 0) & (size_level_next == 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0) 
#         elif ((aMate['is_outsourcing'] == 0) & (size_level_next != 0)): 
#                 appendDict(dict, parent_product , aMate['parent_product'], quota, level, 0)
#         elif((aMate['is_outsourcing'] != 0) & (size_level_next != 0)): 
#                 size_level_next = cal_size_level_next(aMate) 
#                 for i in range(1, size_level_next + 1):
#                 dict["quota_outsourcing"].append(quota)
#                 level = level - (i - 1)
#                 dict["level"].append(level)
#                 dict["size_level_next"].append(size_level_next)
#                 quota = quota * aMate['quota_outsourcing{}'.format(i)]
#                 level = level + 1
#                 dict["parent_product"].append(parent_product)
#                 child_product = aMate['child_product{}'.format(i)]
#                 dict["child_product"].append(product_id)
#                 recursivelyNumberNeed(dict, dfTotalMate, parent_product, child_product, quota, level, size_level_next)
                
                
#         def recursivelyCalculateSecondaryNeed(dfTotalMate):
#         for i in range(0 , len(dfTotalMate)):
#                 aMaterial = dfTotalMate.loc[i]
#                 parent_product = aMaterial['parent_product']
#                 size_level_next = cal_size_level_next(aMaterial)
#                 if (size_level_next == 0): 
#                 level = 1
#                 appendDict(dict, parent_product , 0, 0, level, 0)
#                 else:
#                 for i in range(1 , size_level_next + 1):
#                         quota = 1
#                         level = 2
#                         quota = quota * aMaterial['quota_outsourcing{}'.format(i)]
#                         product_id = aMaterial['child_product{}'.format(i)]
#                         # appendDict(dict, parent_product , child_product, quota, level, size_level_next) 
#                         recursivelyNumberNeed(dict, dfTotalMate, parent_product, product_id, quota, level, size_level_next)
                                
#         return dict