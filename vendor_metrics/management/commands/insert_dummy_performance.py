# In yourapp/management/commands/insert_dummy_historical_data.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from vendor_metrics.models import HistoricalPerformance, Vendor
from random import randint, uniform

class Command(BaseCommand):
    help = 'Inserts dummy data into HistoricalPerformance model'

    def handle(self, *args, **kwargs):
        # Get all vendors
        vendors = Vendor.objects.all()

        for vendor in vendors:
            # Generate dummy data
            date = timezone.now().date()
            on_time_delivery_rate = uniform(0, 1)  # Random value between 0 and 1
            quality_rating_avg = uniform(1, 5)  # Random value between 1 and 5
            average_response_time = randint(1, 100)  # Random integer between 1 and 100
            fulfillment_rate = uniform(0, 1)  # Random value between 0 and 1

            # Create HistoricalPerformance instance
            historical_data = HistoricalPerformance.objects.create(
                vendor=vendor,
                date=date,
                on_time_delivery_rate=on_time_delivery_rate,
                quality_rating_avg=quality_rating_avg,
                average_response_time=average_response_time,
                fulfillment_rate=fulfillment_rate
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully inserted data for {vendor.name}'))
