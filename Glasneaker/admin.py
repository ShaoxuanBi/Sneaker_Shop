from django.contrib import admin
from Glasneaker.models import User, Administrator, Product, Comment, Basket, Order
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email')
    list_per_page = 10

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'email')
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_ID', 'product_name', 'category', 'price', 'size')
    list_per_page = 10

class CommentrAdmin(admin.ModelAdmin):
    list_display = ('comment_number', 'product_ID', 'user_name', 'time')
    list_per_page = 10

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'shoes_name', 'shoes_colour', 'shoes_quantity', 'shoes_size', 'original_price', 'outlet', 'total_price', 'delivery')
    list_per_page = 10

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_ID', 'first_name', 'last_name', 'email', 'phone_number', 'delivery_options')
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentrAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)