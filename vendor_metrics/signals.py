from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendor_metrics.models import PurchaseOrder, HistoricalPerformance
from django.utils import timezone
import threading

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance_metrics(sender, instance, created, **kwargs):
    """
    Update vendor performance metrics upon saving a PurchaseOrder instance.

    Parameters:
        sender (class): The sender class of the signal.
        instance (PurchaseOrder): The instance of PurchaseOrder being saved.
        created (bool): A boolean indicating whether the instance was created or not.
        **kwargs (dict): Additional keyword arguments.

    Returns:
        None
    """
    vendor = instance.vendor
    vendor_po = PurchaseOrder.objects.filter(vendor=vendor)
    completed_orders = vendor_po.filter(
            status=PurchaseOrder.COMPLETED
        )

    # Retrieve the previous status value
    previous_status = instance._state.fields_cache.get('status', None)  # Assuming 'status' is the field name

    # List to store threads
    threads = []

    # Create threads for each metric update task
    if instance.status == PurchaseOrder.COMPLETED:
        t1 = threading.Thread(target=update_on_time_delivery_rate, args=(vendor, instance, completed_orders))
        threads.append(t1)
        if instance.quality_rating:
            t2 = threading.Thread(target=update_quality_rating_avg, args=(vendor, completed_orders))
            threads.append(t2)

    if instance.acknowledgment_date:
        t3 = threading.Thread(target=update_average_response_time, args=(vendor, vendor_po))
        threads.append(t3)

    if previous_status is not None and previous_status != instance.status:
        t4 = threading.Thread(target=update_fulfilment_rate, args=(vendor, completed_orders, vendor_po))
        threads.append(t4)

    # Start all threads
    for thread in threads:
        thread.start()

    # Create or update HistoricalPerformance instance
    create_or_update_historical_performance(vendor)

def update_on_time_delivery_rate(vendor, instance, completed_orders):
    completed_orders_count = completed_orders.count()
    on_time_delivery_count = completed_orders.filter(
        delivery_date__lte=instance.delivery_date).count()

    on_time_delivery_rate = on_time_delivery_count / completed_orders_count if completed_orders_count > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate
    vendor.save()

def update_quality_rating_avg(vendor, completed_orders):
    quality_ratings = [order.quality_rating for order in completed_orders if order.quality_rating]
    quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0

    vendor.quality_rating_avg = quality_rating_avg
    vendor.save()

def update_average_response_time(vendor, vendor_po):
    response_times = [order.acknowledgment_date - order.issue_date for order in vendor_po.filter(acknowledgment_date__isnull=False)]
    avg_response_time = sum(response_times, timedelta()) / len(response_times) if response_times else timedelta()

    vendor.average_response_time = avg_response_time.total_seconds() / 60  # Convert to minutes
    vendor.save()

def update_fulfilment_rate(vendor, completed_orders, vendor_po):
    total_orders = vendor_po.count()
    fulfilled_orders = completed_orders.count()
    fulfilment_rate = fulfilled_orders / total_orders if total_orders > 0 else 0

    vendor.fulfillment_rate = fulfilment_rate
    vendor.save()

def create_or_update_historical_performance(vendor):
    # Create or update HistoricalPerformance instance
    date = timezone.now()
    historical_data, created = HistoricalPerformance.objects.get_or_create(vendor=vendor, date=date)
    historical_data.on_time_delivery_rate = vendor.on_time_delivery_rate
    historical_data.quality_rating_avg = vendor.quality_rating_avg
    historical_data.average_response_time = vendor.average_response_time
    historical_data.fulfillment_rate = vendor.fulfillment_rate
    historical_data.save()
