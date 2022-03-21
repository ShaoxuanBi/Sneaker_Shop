from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(verbose_name='Brand', max_length=128)
    views = models.IntegerField(verbose_name='Follow', default=0)
    likes = models.IntegerField(verbose_name='Collection', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand"
        verbose_name = 'Brand'
        verbose_name_plural = verbose_name


'''
use django.auth.models instead of User and Administrator
Use Django. auth to manage registration and login functions,cancel the User and Administrator tables, need to migrate
'''


# class User(models.Model):
#     username = models.CharField(max_length=64)
#     password = models.CharField(max_length=64)
#     email = models.CharField(max_length=64)
#     fisrtname = models.CharField(max_length=32)
#     lastname = models.CharField(max_length=32)

#     class Meta:
#         db_table = "User"

#     def __str__(self):
#         return self.username


class Product(models.Model):

    brand = models.ForeignKey(
        to='Brand', on_delete=models.DO_NOTHING, verbose_name='Brand', blank=True, null=True)
    productname = models.CharField(max_length=64, verbose_name='Product_name')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    picture = models.CharField(verbose_name='Picture', max_length=128)
    price = models.DecimalField(
        max_digits=16, decimal_places=2, verbose_name='Price', blank=True, null=True)
    quantity = models.IntegerField(
        default=0, verbose_name='Stock', blank=True, null=True)

    class Meta:
        db_table = "Product"
        verbose_name = 'Product_name'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.productname)


class Comment(models.Model):
    commentnumber = models.IntegerField(verbose_name='Comment_number', default=0)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(verbose_name='User_name', max_length=64)
    content = models.TextField(verbose_name='Content', blank=True)
    reply = models.TextField(verbose_name='Reply', blank=True)
    time = models.DateTimeField(verbose_name='Time', auto_now_add=True)

    class Meta:
        db_table = "Comment"
        verbose_name = 'Comment_number'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.commentnumber


class Cart(models.Model):
    shoeid = models.CharField(verbose_name='Shoe_id', max_length=128)
    shoessize = models.DecimalField(
        verbose_name='Size', max_digits=3, decimal_places=1)
    number = models.IntegerField(verbose_name='number', default=1)
    price = models.DecimalField(
        verbose_name='Single_price', max_digits=16, decimal_places=2)
    user = models.CharField(verbose_name='User', max_length=128)

    class Meta:
        db_table = "Cart"
        verbose_name = 'Cart'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    username = models.CharField(verbose_name='User_name', max_length=64)
    address = models.CharField(verbose_name='Adress', max_length=512)
    phonenumber = models.CharField(verbose_name='Phone_number', max_length=16)
    ordernumber = models.CharField(verbose_name='Oder_number', max_length=512)
    price = models.CharField(verbose_name='Total_price', max_length=512)
    paypal = models.BooleanField(verbose_name='Paypal', default=False)

    class Meta:
        db_table = "Order"
        verbose_name = 'Order'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orderID


class Promotion(models.Model):
    promotionID = models.CharField(max_length=64, unique=True)
    promotioncode = models.CharField(max_length=64)

    class Meta:
        db_table = "Promotion"
        verbose_name = 'Promotion'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.promotionID
