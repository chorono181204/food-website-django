# Generated by Django 5.1.2 on 2024-11-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_orderdetails_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Đã xác nhận'), (1, 'Đang giao hàng'), (2, 'Giao hàng thành công')], default=0),
        ),
    ]
