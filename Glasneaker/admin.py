from django.contrib import admin
from Glasneaker.models import User, Administrator, Product, Comment, Basket, Order
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_per_page = 10

class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ('productID', 'productname', 'category', 'price', 'size')
    list_per_page = 10

class CommentrAdmin(admin.ModelAdmin):
    list_display = ('commentnumber', 'productID', 'username', 'time')
    list_per_page = 10

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'shoesname', 'shoescolour', 'shoesquantity', 'shoessize', 'originalprice', 'outlet', 'totalprice', 'delivery')
    list_per_page = 10

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderID', 'firstname', 'lastname', 'email', 'phonenumber', 'deliveryoptions')
    list_per_page = 10


admin.site.register(User, UserAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentrAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)