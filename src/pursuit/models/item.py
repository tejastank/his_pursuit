from django.db import models
from scipy.signal._max_len_seq import max_len_seq
from profiles.models import Profile

class ItemType(models.Model):
    name = models.CharField("Name", max_length=100)
    
    by = models.ForeignKey(Profile, related_name='sales_order_payments', on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)
    
    class Meta:
        app_label = 'pursuit'
        db_table = 'item_type'
        
class ItemQualityType(models.Model):
    name = models.CharField("Name", max_length=100)

    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = "item_quality_type"

class ItemMaterial(models.Model):
    
    #TODO: Verify if these 2 are necessary
    external_code = models.CharField('External Code', max_length=100)
    internal_code = models.CharField('Internal Code', max_length=100)
    unit = models.CharField('Unit', max_length=50, default='yard')
    reference_cost = models.DecimalField('Reference Price', max_digits=10, decimal_places=2)
    description = models.CharField('Description', max_length=500, blank=True, null=True)
    color = models.CharField('Color', max_length=50)

    quality = models.ForeignKey(ItemQualityType, related_name="item_materials", on_delete=models.PROTECT)

    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = 'item_material'

class Item(models.Model):
    
    item_code = models.CharField("Item Code", max_length=20)
    name = models.CharField("Item Name", max_length=100)
    
    item_type = models.ForeignKey(ItemType, related_name="item", on_delete=models.PROTECT)

    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = 'item'