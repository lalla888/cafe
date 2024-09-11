from django.contrib import admin
from .models import Enquiry,burgers,beverage,sandwich,frenchfries,dessert,pizzas
# Register your models here.

@admin.register(Enquiry)
class Admin(admin.ModelAdmin):
    list_display=('name','number','members','date',)

@admin.register(burgers)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')
    
@admin.register(beverage)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')

@admin.register(sandwich)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')

@admin.register(frenchfries)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')

@admin.register(dessert)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')

@admin.register(pizzas)
class Admin(admin.ModelAdmin):
    list_display=('head','price','offers','img1')