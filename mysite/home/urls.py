from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>', views.details, name='details'),
    path('add', views.create_items, name='add'),
    path('update/<int:item_id>', views.update_item, name='update'),

]
