from django.urls import path
from apps.cart.views import *

urlpatterns = [
    path('add', CartAddView.as_view(), name="add"),  # 购物车记录添加
    path('', CartInfoView.as_view(), name="show"),  # 购物车页面显示
    path('update', CartupdateView.as_view(), name="update"),  # 购物车记录更新
    path('delete', CartdeleteView.as_view(), name="delete"),  # 购物车记录删除
]
