from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from . import models

class SalesOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.fields["email"].widget.input_type = "email"  # ugly hack
        
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = models.SalesOrder
        fields = ['customer_name', 'remarks']