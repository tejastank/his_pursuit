from django.conf.urls import url
from rest_framework import routers
from . import views
from . import viewsets

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name="Sales Dashboard"),
    url(r'^create/$', views.CreateSalesOrderView.as_view(), name="Create Sales Order"),
    url(r'^create-post/$', views.CreateSalesView.as_view(), name="Create Sales Order Post"),
    url(r'^sales-order-list/$', views.SalesOrderList.as_view(), name="Sales Order List"),
    url(r'^order/$', views.SalesOrderView.as_view(), name="Sales Order"),

    # ViewSets
    url(r'^list/$', viewsets.SalesOrderListViewSet.as_view({'get': 'list'}), name="Sales List REST"),
    url(r'^rest/order/(?P<id>\d)/$', viewsets.SalesOrderViewSet.as_view({'get': 'list'}), name="Sales Order REST"),
    
    url(r'^customer/create/$', views.CustomerForm.as_view(), name="Create Customer"),
    url(r'^customer/list/$', viewsets.CustomerListViewSet.as_view({'get': 'list'}), name="Customer List REST"),
]
