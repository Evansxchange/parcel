# Generated by Django 4.2.8 on 2023-12-21 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_remove_shippinginfo_city_remove_shippinginfo_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippinginfo',
            name='Est_Delivery_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='delivery_status',
            field=models.CharField(choices=[('pending', 'pending'), ('on-hold', 'on-hold'), ('moving', 'moving'), ('under-inspection', 'under-inspection')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='departure_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='departure_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='destination_service_area',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='origin_service_area',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='paymeny_method',
            field=models.CharField(choices=[('Cash-0n-Delivery', 'Cash-0n-Delivery'), ('Online Payment', 'Online Payment'), ('Pay-To-Bank', 'Pay-To-Bank')], default='Pay-To-Bank', max_length=20),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='qauntity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='receiver_address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='sender_address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='total_charges',
            field=models.PositiveIntegerField(default=2200),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='transportation_mode',
            field=models.CharField(choices=[('Air Freight', 'Air Freight'), ('Road Freight', 'Road Freight'), ('Sea Freight', 'Sea Freight'), ('Express Delivery', 'Express Delivery')], default='Air Freight', max_length=20),
        ),
        migrations.AddField(
            model_name='shippinginfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='waybillNumber',
            field=models.CharField(default='AWB-29746', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
