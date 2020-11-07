from django.contrib import admin
from .models import *

admin.site.register(Exclusive)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Offer)
