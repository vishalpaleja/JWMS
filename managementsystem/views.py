from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InboundForm
from .models import Inbound
from .tables import InventoryTable
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
	return render(request, 'managementsystem/home.html')

@login_required
def inbound(request):
    if request.method == 'POST':    
        form = InboundForm(request.POST)
        if form.is_valid():
            form.save()
            customer = form.cleaned_data.get('customer')
            messages.success(request, f'Item entered for {customer}!')
            return redirect('inventory')
        
    else:
        form = InboundForm()
    return render(request, 'managementsystem/inbound.html', {'form': form})

@login_required
def inventory(request):
    inventory = InventoryTable(Inbound.objects.all())
    return render(request, 'managementsystem/inventory.html', {"inventory": inventory})