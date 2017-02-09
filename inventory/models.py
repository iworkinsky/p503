from django.db import models

# Create your models here.
class Item(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemCode = models.CharField(max_length=50)
    ItemName = models.CharField(max_length=50)
    Remark = models.CharField(max_length=200)
    def __str__(self):
        return self.ItemName
class Inventory(models.Model):
    InventoryId = models.AutoField(primary_key=True)
    Item = models.ForeignKey(Item,null=False)
    Amount = models.IntegerField(null=True)
class InStockBill(models.Model):
    InStockBillId = models.AutoField(primary_key=True)
    InStockBillCode = models.CharField(max_length=40)
    InStockDate = models.DateTimeField(null=True)
    Operator = models.CharField(max_length=40)
    Item = models.ForeignKey(Item,null=False)
    Amount = models.IntegerField(null=True)

