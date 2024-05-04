from rest_framework import generics
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer
from .pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated
from .filters import PurchaseOrderFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg
from django.http import JsonResponse
from django.views import View

class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseOrderFilter

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

class VendorPerformanceView(APIView):
    """
    Retrieve performance metrics for a specific vendor.

    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id):
        """
        Get performance metrics for the specified vendor.

        Parameters:
            vendor_id (int): The ID of the vendor.

        Returns:
            Response: JSON response containing performance metrics.
        """
        try:
            vendor = Vendor.objects.get(id=vendor_id)
            performance_metrics = {
                "on_time_delivery_rate": vendor.on_time_delivery_rate,
                "quality_rating_avg": vendor.quality_rating_avg,
                "average_response_time": vendor.average_response_time,
                "fulfillment_rate": vendor.fulfillment_rate
            }
            return Response(performance_metrics)
        except Vendor.DoesNotExist:
            return Response({"error": "Vendor not found"}, status=404)


class AcknowledgePurchaseOrder(APIView):
    """
    Acknowledge a purchase order.

    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, po_id):
        """
        Acknowledge a purchase order by updating the acknowledgment date.

        Parameters:
            po_id (int): The ID of the purchase order to acknowledge.

        Returns:
            Response: JSON response indicating the result of the acknowledgment.
        """
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()
            return Response({"message": "Purchase order acknowledged successfully"})
        except PurchaseOrder.DoesNotExist:
            return Response({"error": "Purchase order not found"}, status=404)

class VendorPerformanceTrendsView(View):
    """
    A view to provide analysis of vendor performance trends day, week, and month-wise.
    """
    
    def get(self, request, vendor_id):
        """
        Handle GET requests to fetch performance trends for a specific vendor.

        Parameters:
            request (HttpRequest): The request object.
            vendor_id (int): The ID of the vendor.

        Returns:
            JsonResponse: A JSON response containing performance trends.
        """
        try:
            # Get vendor object
            vendor = Vendor.objects.get(pk=vendor_id)
        except Vendor.DoesNotExist:
            return JsonResponse({'error': 'Vendor not found'}, status=404)

        # Get start and end dates for day, week, and month intervals
        today = timezone.localdate()
        start_of_week = today - timedelta(days=today.weekday())
        start_of_month = today.replace(day=1)
        
        # Calculate performance trends for each interval
        day_performance = self.get_performance_data(vendor, today)
        week_performance = self.get_performance_data(vendor, start_of_week)
        month_performance = self.get_performance_data(vendor, start_of_month)

        return JsonResponse({
            'vendor_id': vendor_id,
            'day_performance': day_performance,
            'week_performance': week_performance,
            'month_performance': month_performance
        })

    def get_performance_data(self, vendor, start_date):
        """
        Retrieve performance data for a given interval.

        Parameters:
            vendor (Vendor): The vendor object.
            start_date (datetime.date): The start date of the interval.

        Returns:
            dict: A dictionary containing performance metrics.
        """
        end_date = start_date + timedelta(days=1)
        # Query HistoricalPerformance objects and aggregate performance metrics
        performance_data = HistoricalPerformance.objects.filter(
            vendor=vendor, date__gte=start_date, date__lt=end_date
        ).aggregate(
            on_time_delivery_rate=Avg('on_time_delivery_rate'),
            quality_rating_avg=Avg('quality_rating_avg'),
            average_response_time=Avg('average_response_time'),
            fulfillment_rate=Avg('fulfillment_rate')
        )
        return performance_data