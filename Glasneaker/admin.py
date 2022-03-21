from django.contrib import admin
from django.contrib.auth.models import User
from . import models
# Register your models here.


admin.site.register(models.Brand)
admin.site.register(models.Product)
# admin.site.register(models.Comment)
# admin.site.register(models.Cart)
admin.site.register(models.Order)
# admin.site.register(User)
