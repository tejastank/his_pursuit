from pursuit import models
from pursuit.prefix import Prefix
from profiles.models import Profile
from pursuit.services.id_distributor import IdDistributorService

class SalesOrderService:
    @staticmethod
    def create_sales_order_detail(json_obj_detail, main, user):
        detail = models.SalesOrderDetail()
        detail.row_no = json_obj_detail['no']
        detail.by = Profile.objects.get(user=user)
        detail.quantity = json_obj_detail['quantity']
        detail.unit_price = json_obj_detail['price']
        detail.material = models.ItemMaterial.objects.get(id=1)
        detail.main = main
        
        return detail
    
    @staticmethod
    def create_sales_order(json_obj, user):
        main = models.SalesOrder()
        main.order_id = IdDistributorService.gen_next_id(Prefix.SO)
        main.customer = models.Customer.objects.get(phone = json_obj['cust_phone'])
        main.by = Profile.objects.get(user=user)
        main.sales_staff = main.by
        
        return main

    @staticmethod
    def create(json_obj, user):
        main = SalesOrderService.create_sales_order(json_obj, user)
        main.save()

        details = list(map(lambda d: SalesOrderService.create_sales_order_detail(d, main, user), json_obj['details']))
        
        for d in details:
            d.save()