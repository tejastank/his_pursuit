import datetime
from django.db import models
from .customer import Customer
from .item import ItemMaterial
from profiles.models import Profile

class SalesOrderPayment(models.Model):

    payment_date = models.DateField('Payment Date', default=datetime.date.today)
    remarks = models.CharField('Remarks', max_length=1000, blank=True, null=True)
    amount = models.DecimalField('Amount', max_digits=10, decimal_places=2)
    transaction_id = models.CharField('Transaction Id', max_length=100, blank=True, null=True)
    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = 'sales_order_payment'

class SalesOrder(models.Model):
    
    order_id = models.CharField("Order Id", max_length=20, default=None, unique=True)
    order_date = models.DateField("Order Date", default=datetime.date.today)
    remarks = models.CharField("Remarks", max_length=1000, blank=True, null=True)
    
    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)    
    
    customer = models.ForeignKey(Customer, related_name="sales_orders", on_delete=models.PROTECT)
    sales_staff = models.ForeignKey(Profile, related_name="sales_orders", on_delete=models.PROTECT) 

    class Meta:
        app_label = 'pursuit'
        db_table = 'sales_order'
        permissions = (
            ("view_salesorder", "Can view sales order"),
        )
        
class SalesOrderDetail(models.Model):
    
    row_no = models.IntegerField("Row No")
    quantity = models.IntegerField("Quantity")
    unit_price = models.DecimalField("Unit Price", max_digits=10, decimal_places=2)
    promotion_price = models.DecimalField("Promotion Price", max_digits=10, decimal_places=2, blank=True, null=True)
    
    material = models.ForeignKey(ItemMaterial, related_name="salesorder_details", on_delete=models.PROTECT)
    main = models.ForeignKey(SalesOrder, related_name='salesorder_details', on_delete=models.PROTECT)
    
    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)
    
    class Meta:
        app_label = 'pursuit'
        db_table = 'sales_order_detail'