# Generated by Django 4.2.8 on 2023-12-25 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_shippinginfo_delivery_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippinginfo',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='waybillNumber',
            field=models.CharField(default='AWB-29746', max_length=10, unique=True),
        ),
    ]
