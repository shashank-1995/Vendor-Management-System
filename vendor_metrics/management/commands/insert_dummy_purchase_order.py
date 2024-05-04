import random
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from vendor_metrics.models import PurchaseOrder, Vendor


class Command(BaseCommand):
    help = 'Insert random data into the PurchaseOrder table'

    def handle(self, *args, **options):
        vendors = Vendor.objects.all()

        # Keep track of generated PO numbers to ensure uniqueness
        generated_po_numbers = set()

        for _ in range(100):
            # Generate a unique PO number
            while True:
                po_number = f'PO-{random.randint(1000, 9999)}'
                if po_number not in generated_po_numbers:
                    generated_po_numbers.add(po_number)
                    break

            # Rest of the data generation logic remains the same
            vendor = random.choice(vendors)
            order_date = timezone.now() - timedelta(days=random.randint(1, 365))
            delivery_date = order_date + timedelta(days=random.randint(1, 30))
            items = [{'name': f'Item {i}', 'price': random.randint(1, 100)} for i in range(random.randint(1, 5))]
            quantity = random.randint(1, 100)
            status = random.choice(['pending', 'canceled', 'completed'])
            quality_rating = random.uniform(1.0, 5.0) if status == 'completed' else None
            issue_date = order_date - timedelta(days=random.randint(1, 10))
            acknowledgment_date = delivery_date if status == 'completed' else None

            # Ensure quality_rating is None if status is not 'Completed'
            if status != 'completed':
                quality_rating = None

            PurchaseOrder.objects.create(
                po_number=po_number,
                vendor=vendor,
                order_date=order_date,
                delivery_date=delivery_date,
                items=items,
                quantity=quantity,
                status=status,
                quality_rating=quality_rating,
                issue_date=issue_date,
                acknowledgment_date=acknowledgment_date
            )

        self.stdout.write(self.style.SUCCESS('Successfully inserted 10 random PurchaseOrder records'))
