from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from .models import Book

def index(request):
    item_list = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))