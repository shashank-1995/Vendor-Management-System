# Generated by Django 4.2.11 on 2024-05-04 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=50, unique=True)),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('po_number', models.CharField(db_index=True, max_length=100, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('canceled', 'canceled')], default='pending', max_length=50)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_metrics.vendor')),
            ],
            options={
                'indexes': [models.Index(fields=['order_date'], name='vendor_metr_order_d_e59e0b_idx'), models.Index(fields=['quantity'], name='vendor_metr_quantit_02b63b_idx'), models.Index(fields=['status'], name='vendor_metr_status_1cb8d8_idx')],
            },
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_metrics.vendor')),
            ],
            options={
                'indexes': [models.Index(fields=['date'], name='vendor_metr_date_6df72e_idx')],
            },
        ),
    ]
