from django.db import models
from .managers import BaseModelManager

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True

class Vendor(BaseModel):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return self.name

class PurchaseOrder(BaseModel):
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    STATUS_TYPES = (
        (PENDING, 'pending'),
        (COMPLETED, 'completed'),
        (CANCELED, 'canceled'),
    )
    po_number = models.CharField(max_length=100, unique=True, db_index=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_index=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS_TYPES, default=PENDING, max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number
    
    class Meta:
        indexes = [
            models.Index(fields=['order_date']),
            models.Index(fields=['quantity']),
            models.Index(fields=['status']),
        ]

class HistoricalPerformance(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_index=True)
    date = models.DateField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    
    class Meta:
        indexes = [
            models.Index(fields=['date']),
        ]