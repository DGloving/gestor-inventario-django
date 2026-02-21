from django.contrib import admin
from .models import Category, Supplier, Product, Sale


admin.site.register(Category)
admin.site.register(Supplier)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'sale_date')
    list_filter = ('sale_date', 'product')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'stock_quantity', 'price_cost', 'price_sell', 'lucro')
    list_filter = ('category', 'supplier')
    search_fields = ('name', 'sku')

    def lucro(self, obj):
        return f"R$ {obj.price_sell - obj.price_cost}"
    
    lucro.short_description = 'Lucro Unitário'