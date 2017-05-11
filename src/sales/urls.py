from django.conf.urls import url
from .views import Dashboard, CreateSalesOrderView

urlpatterns = [
    url(r'^dashboard/$', Dashboard.as_view(), name="Sales Dashboard"),
    url(r'^create-sales-order/$', CreateSalesOrderView.as_view(), name= "Create Sales Order"),
]
