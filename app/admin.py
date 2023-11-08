from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced  # Corrected model names

# Register your models here.
@admin.register(Customer)  # Corrected model name
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discount_price', 'brand', 'category', 'product_image']  # Corrected field name

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'customer', 'product', 'quantity', 'ordered_date', 'status']  # Corrected field name
