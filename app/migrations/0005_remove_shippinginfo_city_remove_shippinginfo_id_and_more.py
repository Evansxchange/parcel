# Generated by Django 4.2.8 on 2023-12-21 09:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_item_des_shippinginfo_item_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippinginfo',
            name='city',
        ),
        migrations.RemoveField(
            model_name='shippinginfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='waybillNumber',
            field=models.PositiveBigIntegerField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
