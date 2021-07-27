# from django.contrib import admin
from django.urls import path

from .views import home_page, product_list, product_detail, create_product, update_product, delete_product

from .class_view import *

urlpatterns = [

    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create-product'),
    path('product/update/<int:id>/', ProductUpdateView.as_view(), name='update-product'),
    path('product/delete/<int:id>/', ProductDeleteView.as_view(), name='delete-product')
]