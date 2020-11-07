from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL
from django.shortcuts import render, reverse
from django.utils.text import slugify

# Create your models here.


class Exclusive(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    thumbnail = models.ImageField(upload_to='exclusive')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name


class Product(models.Model):
    # category = models.ForeignKey(Categories,
    #                              on_delete=SET_NULL,
    #                              null=True,
    #                              blank=True)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    price = models.FloatField()
    thumbnail = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class Offer(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    thumbnail = models.ImageField(upload_to='offer')


class Order(models.Model):
    customer = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_subtotal for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.value for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    value = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

    @property
    def get_subtotal(self):
        subtotal = self.product.price * self.value
        return subtotal
