from django.contrib import admin
from . import models


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ['__str__', 'price', 'rating', 'is_active', 'category']
    list_filter = ['is_active']
    list_editable = ['is_active']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductInformation)