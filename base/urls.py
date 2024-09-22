from django.contrib import admin
from django.urls import path, include
from base import views
from rest_framework.routers import DefaultRouter

# CONNECT END POINTS IN THE APP FROM VIEWS FILE
urlpatterns = [
    path('', views.index),
    path('products', views.product_list),
    path('products/<pk>', views.product_detail),
    path('product/<pk>', views.product_update),
    path('product', views.product_create),
    path('product_del/<pk>', views.product_delete),
]
