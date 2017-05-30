from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from pursuit.models.sales import SalesOrder
from pursuit.models.customer import Customer

class SalesOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = SalesOrder
        fields = ['order_date', 'remarks', 'customer', 'sales_staff']
        
class CustomerForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout.append(Submit('save', 'save'))
        
    class Meta:
        model = Customer
        exclude = ['by', 'at']
        #fields = ['name','phone','occupation','dob','refer_by','email','office_address','delivery_address']
    
    #def save(self, force_insert=False, force_update=False, commit=True):
    #    super(Customer, self).save(commit=True)
class CustomerView(forms.ModelForm):

    def __init__(self,*args,**kwargs):      
        super(CustomerView,self).__init__(*args, **kwargs)    

        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout.append(Submit('save','save'))

    class Meta :
        model = Customer
        exclude = ['by','at']

    