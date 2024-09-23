from django.contrib import admin
from django.urls import path, include
from base import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView


# CONNECT END POINTS IN THE APP FROM VIEWS FILE
urlpatterns = [
    path('', views.index),
    path('products', views.product_list),
    path('products/<pk>', views.product_detail),
    path('product/<pk>', views.product_update),
    path('product', views.product_create),
    path('product_del/<pk>', views.product_delete),

    path('students', views.student_list),
    path('students/<pk>', views.student_detail),
    path('student/<pk>', views.student_update),
    path('student', views.student_create),
    path('student_del/<pk>', views.student_delete),
    path('login/', TokenObtainPairView.as_view()),
]
