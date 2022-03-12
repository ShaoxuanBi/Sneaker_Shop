from django.db import models

class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    fisrtname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

    class Meta:
        db_table="User"

    def __str__(self):
        return self.username

class Administrator(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    fisrtname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)

    class Meta:
        db_table="Administrator"

    def __str__(self):
        return self.username

class Product(models.Model):
    productID = models.IntegerField(default=0, unique=True)
    productname = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="static/image", blank=True)
    category = models.CharField(max_length=32)
    price = models.DecimalField(max_digits =16,decimal_places =2)
    quantity = models.CharField(max_length=16)
#   username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)      #seller name
    size = models.CharField(max_length=16)

    class Meta:
        db_table="Product"

    def __str__(self):
        return self.productname

class Comment(models.Model):
    commentnumber = models.IntegerField(default=0, unique=True)
    productID = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)       # the name of the person who left the message
    content = models.TextField(blank=True)
    reply = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Comment"

    def __str__(self):
        return self.commentnumber

class Basket(models.Model):
    shoesname = models.CharField(max_length=64)
    shoescolour = models.CharField(max_length=16)
    shoesquantity = models.IntegerField(default=1)
    shoessize = models.DecimalField(max_digits =3,decimal_places =1)
    originalprice = models.DecimalField(max_digits =16,decimal_places =2)
    outlet = models.DecimalField(max_digits =16,decimal_places =2)
    totalprice = models.DecimalField(max_digits =16,decimal_places =2)
    delivery = models.CharField(max_length=128)

    class Meta:
        db_table="Basket"

    def __str__(self):
        return self.shoesname

class Order(models.Model):
    orderID = models.IntegerField(default=0, unique=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    findaddress = models.CharField(max_length=512)
    phonenumber = models.CharField(max_length=16)
    deliveryoptions = models.CharField(max_length=16)
    cardnumber = models.IntegerField(default=0)
    expirationdate = models.IntegerField(default=0)
    securitycode = models.IntegerField(default=0)
    paypal = models.URLField()
    klarna = models.URLField()
    
    class Meta:
        db_table="Order"

    def __str__(self):
        return self.orderID

class Promotion(models.Model):
    promotionID = models.CharField(max_length=64, unique=True)
    promotioncode = models.CharField(max_length=64)

    class Meta:
        db_table="Promotion"

    def __str__(self):
        return self.promotionID
