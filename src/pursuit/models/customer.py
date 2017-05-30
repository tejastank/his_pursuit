from django.db import models
from profiles.models import Profile

class Customer(models.Model):

    name = models.CharField("Name", max_length=100)
    phone = models.CharField('Phone Number', max_length=20, unique=True)
    occupation = models.CharField('Occupation', max_length=100, blank=True, null=True)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    refer_by = models.CharField('Refered By', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    office_address = models.CharField('Office Address', max_length=500, blank=True, null=True)
    delivery_address = models.CharField('Delivery Address', max_length=500, blank=True, null=True)

    by = models.ForeignKey(Profile, on_delete=models.PROTECT)
    at = models.DateTimeField('At', auto_now_add=True)

    class Meta:
        app_label = 'pursuit'
        db_table = 'customer'

    def __unicode__(self):      
        return self.name