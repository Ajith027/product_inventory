from django.contrib import admin
from django.urls import path, include

from product_inventoryapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('add_warehouse',views.add_warehouse,name='add_warehouse'),
    path('add_category', views.add_category, name='add_category'),
    path('add_product', views.add_product, name='add_product'),
    path('stock',views.stock,name='stock'),
    path('unstock',views.unstock,name='unstock'),
    path('warehouse',views.warehouse,name='warehouse'),
    path('products', views.products, name='products'),
    path('ware_prod/<int:id>', views.ware_prod, name='ware_prod'),

]