# coding:utf-8
from django.http import  HttpResponse
from django.shortcuts import render,render_to_response

#from .models import InStockBill,Item
from django.template import RequestContext
#from .forms import *
from inventory.forms import *
from inventory.models import *

# Create your views here.

def AddInStockBill(request):
    if request.method == 'POST':
        form = InStockBillForm(request.POST)
       #
        if form.is_valid():
            cd = form.cleaned_data
            inStockBill = InStockBill()
            inStockBill.InStockBillCode = cd['fInStockBillCode']
            inStockBill.InStockDate = cd['fInStockDate']
            inStockBill.Amount = cd['fAmount']
            inStockBill.Operator = cd['fOperator']
            inStockBill.Item = cd['fItem']
            inStockBill.save()
            return HttpResponse("/success/")
    else:
            form = InStockBillForm()

           # return HttpResponse("ok2!")
    return render_to_response('InStockAdd.html',{'form':form},context_instance=RequestContext(request))
            #return render_to_response('InStockAdd.html', {'form': form})
def success(request):
    return HttpResponse("表单提交成功！")

def AddItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            item = Item()
            item.ItemCode = cd['ItemCode']
            item.ItemName = cd['ItemName']
            item.save()
            return HttpResponse("Item记录增加成功！")
    else:
        form = ItemForm()
    return render_to_response('ItemAdd.html',{'form':form},context_instance=RequestContext(request))

