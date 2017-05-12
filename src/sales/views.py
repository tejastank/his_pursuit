#from django.shortcuts import render
from django.views import generic
from . import models
from . import forms
from django.contrib.auth.decorators import login_required, permission_required
from braces import views as bracesviews
from django.core.urlresolvers import reverse_lazy

#from sales.models import SalesOrder

# Create your views here.
class Dashboard(bracesviews.LoginRequiredMixin,
                bracesviews.PermissionRequiredMixin,
                generic.TemplateView):
    
    permission_required = "sales.view_salesorder"
    template_name = "sales/dashboard.html"

class CreateSalesOrderView(generic.CreateView):
    form_class = forms.SalesOrderForm
    model = models.SalesOrder
    
    template_name = 'sales/create_sales_order.html'
    success_url = reverse_lazy('home')
    form_valid_message = "You're signed up!"
    