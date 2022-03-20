from django.db import models
from django.contrib.auth.models import User

# glasneaker models


class Brand(models.Model):
    name = models.CharField(verbose_name='品牌名', max_length=128)
    views = models.IntegerField(verbose_name='关注', default=0)
    likes = models.IntegerField(verbose_name='收藏', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Brand"
        verbose_name = '品牌'
        verbose_name_plural = verbose_name


'''
use django.auth.models instead of User and Administrator
用 django.auth管理注册和登录功能,取消User和Administrator的数据表,需要重新migrate
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
        to='Brand', on_delete=models.DO_NOTHING, verbose_name='品牌', blank=True, null=True)
    productname = models.CharField(max_length=64, verbose_name='商品名')
    description = models.TextField(verbose_name='描述', blank=True, null=True)
    picture = models.CharField(verbose_name='图片', max_length=128)
    price = models.DecimalField(
        max_digits=16, decimal_places=2, verbose_name='价格', blank=True, null=True)
    quantity = models.IntegerField(
        default=0, verbose_name='库存', blank=True, null=True)

    class Meta:
        db_table = "Product"
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.productname)


class Comment(models.Model):
    commentnumber = models.IntegerField(verbose_name='品论数', default=0)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(verbose_name='用户名', max_length=64)
    content = models.TextField(verbose_name='内容', blank=True)
    reply = models.TextField(verbose_name='回复', blank=True)
    time = models.DateTimeField(verbose_name='时间', auto_now_add=True)

    class Meta:
        db_table = "Comment"
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.commentnumber


class Cart(models.Model):
    """应改用redis实现"""
    shoeid = models.CharField(verbose_name='鞋子款式', max_length=128)
    shoessize = models.DecimalField(
        verbose_name='鞋码', max_digits=3, decimal_places=1)
    number = models.IntegerField(verbose_name='数量', default=1)
    price = models.DecimalField(
        verbose_name='单价', max_digits=16, decimal_places=2)
    user = models.CharField(verbose_name='用户', max_length=128)

    class Meta:
        db_table = "Cart"
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    username = models.CharField(verbose_name='用户', max_length=64)
    address = models.CharField(verbose_name='地址', max_length=512)
    phonenumber = models.CharField(verbose_name='手机号', max_length=16)
    ordernumber = models.CharField(verbose_name='订单号', max_length=512)
    price = models.CharField(verbose_name='总价', max_length=512)
    paypal = models.BooleanField(verbose_name='是否支付', default=False)

    class Meta:
        db_table = "Order"
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orderID


class Promotion(models.Model):
    promotionID = models.CharField(max_length=64, unique=True)
    promotioncode = models.CharField(max_length=64)

    class Meta:
        db_table = "Promotion"
        verbose_name = '促销'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.promotionID
