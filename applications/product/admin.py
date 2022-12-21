from django.contrib import admin

from applications.product.models import Category, Product, Image

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)