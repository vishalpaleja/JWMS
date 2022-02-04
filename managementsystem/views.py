from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import InboundForm
# Create your views here.

def home(request):
	return render(request, 'managementsystem/home.html')

def inbound(request):
    if request.method == 'POST':    
        form = InboundForm(request.POST)
        if form.is_valid():
            form.save()
            customer = form.cleaned_data.get('customer')
            messages.success(request, f'Order created for {customer}!')
            return redirect('inbound')
    else:
        form = InboundForm()
    return render(request, 'managementsystem/inbound.html', {'form': form})
