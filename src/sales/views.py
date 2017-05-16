from . import forms
from .services.salesorder import SalesOrderService
from braces import views as bracesviews
import json
from pursuit import models
from profiles.models import Profile
from django.views import generic, View
from django.core.urlresolvers import reverse_lazy
from django.http import StreamingHttpResponse

# Create your views here.
class Dashboard(bracesviews.LoginRequiredMixin,
                bracesviews.PermissionRequiredMixin,
                generic.TemplateView):
    
    permission_required = "sales.view_salesorder"
    template_name = "dashboard.html"

class CreateSalesOrderView(generic.TemplateView):
    #form_class = forms.SalesOrderForm
    #model = models.SalesOrder
    
    template_name = 'create_sales_order.html'
    #success_url = reverse_lazy('home')
    #form_valid_message = "You're signed up!"
    
class SalesOrderList(generic.TemplateView):
    template_name = 'sales_order_list.html'

class SalesOrderView(generic.TemplateView):
    template_name = 'sales_order.html'
    
class CustomerForm(generic.CreateView):
    form_class = forms.CustomerForm
    model = models.Customer
    
    template_name = 'create_customer.html'
    success_url = reverse_lazy('home')
    form_valid_message = "Customer Created"
    
    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.by = Profile.objects.get(user=self.request.user)
        customer.save()
        
        return super(CustomerForm, self).form_valid(form)

class CreateSalesView(View):
    def post(self, request):
        json_obj = json.loads(request.body.decode("utf-8"))
        SalesOrderService.create(json_obj, self.request.user)
        return StreamingHttpResponse('it was post request: '+str(json_obj['cust_phone']))
        