from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone_no = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=21, null=True)
    category = models.CharField(max_length=200)
    sub_category1 = models.CharField(max_length=200, null=True)
    sub_category2 = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    description = models.TextField()
    negotiation = models.BooleanField(default=False, null=True, blank=False)
    img = models.ImageField(upload_to='pics', null=True, blank=True)
    contact_info = models.TextField()
    urgent = models.BooleanField(default=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse("pdescription", kwargs={"pk": self.pk})

    def get_add_to_whishlist_url(self):
        return reverse("add_to_whishlist", kwargs={"pk": self.pk})

    @property
    def imageUrl(self):
        try:
            url = self.img.url

        except:
            url = ''
        return url


# class Whishlist(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     product =models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
#     customer =models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False,null=True, blank=False)
#     transaction_id= models.CharField(max_length=150,null=True)


# class Whishlist_item(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     product =models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
#     Whishlist =models.ForeignKey(Whishlist,on_delete=models.SET_NULL,blank=True,null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
    # quantity = models.IntegerField(default=0,null=True,blank=True)


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(WishlistItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:10]
