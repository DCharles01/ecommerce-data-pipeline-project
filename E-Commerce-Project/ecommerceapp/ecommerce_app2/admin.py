from django.contrib import admin

# Register your models here.
from .models import Products, Aisles, Departments, Orders, OrderProducts, Inventory

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):

    # create display for products
    list_display = ("product_id", "product_name", "aisle_id", "department_id", "price")

    # # create filter for products
    # list_filter = ("product_id", "product_name", "aisle_id", "department_id")

    # search bar in admin
    search_fields = ["product_id", "product_name", "aisle_id", "department_id"]


# admin.site.register(Products, ProductsAdmin)

@admin.register(Aisles)
class AislesAdmin(admin.ModelAdmin):

    # create display for products
    list_display = ("aisle_id", "aisle")

    # # create filter for products
    # list_filter = ("aisle_id", "aisle")

    # search bar in admin
    search_fields = ("aisle_id", "aisle")


# admin.site.register(Aisles, AislesAdmin)


@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department')
    list_filter = ('department',)
    list_display = ('department_id', 'department')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'eval_set', 'order_number', 'order_dow', 'order_hour_of_day',
                    'days_since_prior_order')
    # list_filter = ('order_dow', 'order_hour_of_day')
    search_fields = ('order_id', 'user_id', 'order_number', 'order_dow', 'order_hour_of_day')
    
@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product_id', 'add_to_cart_order', 'reordered')
    # list_filter = ('order_id', 'product_id')
    search_fields = ('order_id', 'product_id')


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'aisle_id', 'department_id', 'quantity', 'last_updated')
    # list_filter = ('product_id', 'product_id')
    search_fields = ('product_id', 'aisle_id', 'department_id')



