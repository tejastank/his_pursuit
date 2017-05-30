from django.contrib import admin
from pursuit.models.customer import Customer
from  pursuit.models.sales import SalesOrderPayment,SalesOrder,SalesOrderDetail
# Register your models here.
admin.site.register(Customer)
admin.site.register(SalesOrder)
# admin.site.register(SalesOrderDetail)
admin.site.register(SalesOrderPayment)

