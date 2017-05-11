from django.db import models

# Create your models here.
class SalesOrder(models.Model):
    customer_name = models.CharField("Customer Name", max_length=100)
    remarks = models.CharField("Remarks", max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'sales_order'
        permissions = (
            ("view_salesorder", "Can view sales order"),
        )
        
class SalesOrderDetail(models.Model):
    unit_price = models.DecimalField("Unit Price", max_digits=6, decimal_places=2)
    main = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'sales_order_details'