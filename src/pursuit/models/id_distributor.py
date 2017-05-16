from django.db import models

class IdDistributor(models.Model):
    prefix = models.CharField('Prefix', max_length=20, unique=True)
    last_id = models.IntegerField('Last Id')
    at = models.DateTimeField('At', auto_now_add=True)
    
    class Meta:
        app_label = 'pursuit'
        db_table = 'id_distributor'