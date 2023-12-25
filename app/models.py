from django.db import models
from uuid import uuid4
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
shipment_content = (
 ('cargo', 'cargo'),
 ('parcel', 'parcel'),
 ('document', 'document')
)

paymeny_method = (
 ('Cash-0n-Delivery', 'Cash-0n-Delivery'),
 ('Online Payment', 'Online Payment'),
 ('Pay-To-Bank', 'Pay-To-Bank')
)

transportation_mode = (
 ('Air Freight', 'Air Freight'),
 ('Road Freight', 'Road Freight'),
 ('Sea Freight', 'Sea Freight'),
 ('Express Delivery', 'Express Delivery')
)

delivery_status = (
 ('pending', 'pending'),
 ('on-hold', 'on-hold'),
 ('moving', 'moving'),
 ('cancel', 'cancel'),
 ('under-inspection', 'under-inspection')
)


class ShippingInfo(models.Model):
 id = models.IntegerField( primary_key=True, default=0, unique=True)
 shipperName = models.CharField(max_length=50, help_text="sender's name", null=False)
 shipperNumber = PhoneNumberField( help_text="sender's number")
 shipperemail = models.EmailField( help_text="sender's email", null=False)
 sender_address = models.CharField(max_length=60, null=True)
 receiverName = models.CharField(max_length=50,  help_text="receiver's name", null=False)
 receiverNumber = PhoneNumberField(help_text="receiver's number")
 receiveremail = models.EmailField(help_text="receiver's email", null=False)
 receiver_address = models.CharField(max_length=60, null=True)
 waybillNumber = models.CharField(unique=True, max_length=10, default="AWB-29746",null=False, blank=False)
 shipment_content = models.CharField(max_length=20, choices=shipment_content)
 item_description = models.CharField(max_length=30, help_text="item descriptions")
 weight = models.IntegerField(default=35)
 qauntity = models.PositiveIntegerField(default=1)
 total_charges = models.PositiveIntegerField(default=2200)
 paymeny_method = models.CharField(max_length=20, default="Pay-To-Bank", choices=paymeny_method)
 departure_date = models.DateField(null=True)
 departure_time = models.TimeField(default=timezone.now)
 Est_Delivery_date = models.DateField(null=True)
 origin_service_area = models.CharField(max_length=60, null=True)
 destination_service_area = models.CharField(max_length=60, null=True)
 transportation_mode = models.CharField(max_length=20, default="Air Freight", choices=transportation_mode)
 delivery_status = models.CharField(max_length=20, default="pending", null=False, choices=delivery_status)
 user = models.ForeignKey(User, default="admin", null=True, on_delete=models.CASCADE)

