from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    class Meta:
        db_table="User"

    def __str__(self):
        return self.user_name

class Administrator(models.Model):
    user_name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=64)

    class Meta:
        db_table="Administrator"

    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_ID = models.IntegerField(default=0, unique=True)
    product_name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to="static/image", blank=True)
    category = models.CharField(max_length=32)
    price = models.DecimalField(max_digits =16,decimal_places =2)
    quantity = models.CharField(max_length=16)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)      #seller name
    size = models.CharField(max_length=16)

    class Meta:
        db_table="Product"

    def __str__(self):
        return self.product_name

class Comment(models.Model):
    comment_number = models.IntegerField(default=0, unique=True)
    product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64)       # the name of the person who left the message
    content = models.TextField(blank=True)
    reply = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Comment"

    def __str__(self):
        return self.comment_number

class Basket(models.Model):
    shoes_name = models.CharField(max_length=64)
    shoes_colour = models.CharField(max_length=16)
    shoes_quantity = models.IntegerField(default=1)
    shoes_size = models.DecimalField(max_digits =3,decimal_places =1)
    original_price = models.DecimalField(max_digits =16,decimal_places =2)
    outlet = models.DecimalField(max_digits =16,decimal_places =2)
    total_price = models.DecimalField(max_digits =16,decimal_places =2)
    delivery = models.CharField(max_length=128)

    class Meta:
        db_table="Basket"

    def __str__(self):
        return self.shoes_name

class Order(models.Model):
    order_ID = models.IntegerField(default=0, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    find_address = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=16)
    delivery_options = models.CharField(max_length=16)
    card_number = models.IntegerField(default=0)
    expiration_date = models.IntegerField(default=0)
    security_code = models.IntegerField(default=0)
    paypal = models.URLField()
    klarna = models.URLField()
    
    class Meta:
        db_table="Order"

    def __str__(self):
        return self.order_ID


