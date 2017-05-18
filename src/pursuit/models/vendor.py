from django.db import models
from profiles.models import Profile

class VendorType(models.Model):
    name = models.CharField("Vendor Type", max_length=100, unique=True)
    is_active = models.BooleanField("Is Active", default=True)
    
    class Meta:
        app_label = 'pursuit'
        db_table = 'vendor_type'
    
class Vendor(models.Model):

    name = models.CharField("Vendor Name", max_length=100, unique=True)
    phone = models.CharField('Phone Number', max_length=40, unique=True)
    address = models.CharField('Address', max_length=100, blank=True, null=True)
    vendor_type = models.ForeignKey(VendorType, on_delete=models.PROTECT)

    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = 'vendor'