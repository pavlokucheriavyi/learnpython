from django.contrib import admin
from .models import Products, Categories
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Products, ProductsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories, CategoriesAdmin)