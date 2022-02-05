from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jwms-home'),
    path('inbound', views.inbound, name='inbound'),
    path('inventory', views.inventory, name='inventory'),
]