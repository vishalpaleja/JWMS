import django_tables2 as tables
from .models import Inbound

class InventoryTable(tables.Table):
    class Meta:
        model = Inbound