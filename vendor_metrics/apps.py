from django.apps import AppConfig


class VendorMetricsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_metrics'

    def ready(self):
        import vendor_metrics.signals
