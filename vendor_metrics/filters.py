import django_filters
from .models import PurchaseOrder

class PurchaseOrderFilter(django_filters.FilterSet):
    class Meta:
        model = PurchaseOrder
        fields = ['vendor', 'status', 'order_date']
