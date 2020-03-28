from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
    


def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('home/index.html')
    context = {
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))


def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'home/detail.html',context)

def create_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home:index')

    return render(request,'home/item-form.html',{'form':form})


def update_item(request,item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('home:index')

    return render(request,'home/item-form.html',{'form':form,'item':item})
