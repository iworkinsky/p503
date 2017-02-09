# -*- coding:utf-8 -*-
from django import forms
from .models import Item
class ItemForm(forms.Form):
    ItemCode = forms.CharField(max_length=10,label=u'零件编码',error_messages={'invalid':u'必填项'})
    ItemName = forms.CharField(label=u'零件名称',error_messages={'invalid':u'必填项'})
    Remark = forms.CharField(label=u'备注',required=False,widget=forms.Textarea)

class InStockBillForm(forms.Form):
    fInStockBillCode = forms.CharField(label=u'入库单号')
    fOperator = forms.CharField(label=u'制单人')
    fInStockDate = forms.DateTimeField(label=u'入库时间')
    fAmount = forms.IntegerField(label=u'数量')
    fItem = forms.ModelChoiceField(label=u'零件',queryset = Item.objects.all(),required=True)