from django.urls import path
from .views import (
    VendorListCreateView, 
    VendorRetrieveUpdateDeleteView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDeleteView,
    VendorPerformanceView,
    AcknowledgePurchaseOrder,
    VendorPerformanceTrendsView,
)

urlpatterns = [
    # Vendor Endpoints
    path('vendors/', VendorListCreateView.as_view(), name='vendor_list_create'),  # Endpoint to list vendors and create new vendors
    path('vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor_retrieve_update_delete'),  # Endpoint to retrieve, update, or delete a specific vendor
    
    # Purchase Order Endpoints
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchaseorder-list-create'),  # Endpoint to create a new purchase order
    path('purchase_orders/list/', PurchaseOrderListCreateView.as_view(), name='purchaseorder-list'),  # Endpoint to list all purchase orders with optional filtering by vendor
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchaseorder-retrieve-update-delete'),  # Endpoint to retrieve, update, or delete a specific purchase order

    # Performace Metrics Endpoints
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'), # Endpoint to get current performance of the vendor
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge_purchase_order'), # Endpoint to update po acknowledge date
    path('vendors/<int:vendor_id>/trend/', VendorPerformanceTrendsView.as_view(), name='vendor_performance_trends'),
]
