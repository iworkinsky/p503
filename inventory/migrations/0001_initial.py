# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InStockBill',
            fields=[
                ('InStockBillId', models.AutoField(primary_key=True, serialize=False)),
                ('InStockBillCode', models.CharField(max_length=40)),
                ('InStockDate', models.DateTimeField(null=True)),
                ('Operator', models.CharField(max_length=40)),
                ('Amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('InventoryId', models.AutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemId', models.AutoField(primary_key=True, serialize=False)),
                ('ItemCode', models.CharField(max_length=50)),
                ('ItemName', models.CharField(max_length=50)),
                ('Remark', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='inventory',
            name='Item',
            field=models.ForeignKey(to='inventory.Item'),
        ),
        migrations.AddField(
            model_name='instockbill',
            name='Item',
            field=models.ForeignKey(to='inventory.Item'),
        ),
    ]
