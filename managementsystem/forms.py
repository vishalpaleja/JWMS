from django import forms 
from .models import Inbound

class InboundForm(forms.ModelForm):
    trackingNumber = forms.CharField()
    customer = forms.CharField()
    address = forms.CharField()
    
    class Meta:
        model = Inbound
        fields = ['trackingNumber', 'customer', 'address']
