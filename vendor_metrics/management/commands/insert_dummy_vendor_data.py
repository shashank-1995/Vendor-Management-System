from django.core.management.base import BaseCommand
from django.utils import timezone
from vendor_metrics.models import Vendor
import random
import string

class Command(BaseCommand):
    help = 'Insert random vendors into the Vendor table'

    def handle(self, *args, **kwargs):
        num_entries = 100
        self.insert_random_vendors(num_entries)
        self.stdout.write(self.style.SUCCESS(f'{num_entries} random entries inserted into the Vendor table.'))

    def generate_random_string(self, length):
        """Generate a random string of specified length."""
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_unique_vendor_code(self):
        """Generate a unique vendor code."""
        vendor_code = 'VENDOR' + str(random.randint(100, 999))
        while Vendor.objects.filter(vendor_code=vendor_code).exists():
            vendor_code = 'VENDOR' + str(random.randint(100, 999))
        return vendor_code

    def generate_random_vendor(self):
        """Generate a random vendor object."""
        return Vendor(
            name=self.generate_random_string(20),
            contact_details=self.generate_random_string(20) + '@example.com',
            address=self.generate_random_string(30) + ', City, Country',
            vendor_code=self.generate_unique_vendor_code(),
            on_time_delivery_rate=random.uniform(0.8, 1.0),
            quality_rating_avg=random.uniform(3.0, 5.0),
            average_response_time=random.uniform(1.0, 10.0),
            fulfillment_rate=random.uniform(0.8, 1.0),
            created=timezone.now()
        )

    def insert_random_vendors(self, num_entries):
        """Insert random vendors into the database."""
        for _ in range(num_entries):
            vendor = self.generate_random_vendor()
            vendor.save()
