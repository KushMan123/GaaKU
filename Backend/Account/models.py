from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


from store.models import Product, Comment

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, verbose_name='email address')
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dob = models.DateField(verbose_name='date of birth', null=True)
    batch = models.SmallIntegerField(null=True)
    department = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=50, null=True)
    semester = models.SmallIntegerField(null=True)
    phone_no = models.CharField(max_length=15, null=True)
    image = models.ImageField(default='default.png', upload_to='media')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class NotificationCount(models.Model):
    old = models.IntegerField(default=0)
    updated = models.IntegerField(default=0)
    seen = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class History(models.Model):
    sold_to = models.CharField(max_length=20, default='user')
    product = models.CharField(max_length=20, default='product')
    productname = models.CharField(max_length=50, default='product')
    productcategory = models.CharField(max_length=50, default='product')
    productprice = models.IntegerField(default=0)
    productimg = models.ImageField(upload_to='pics', null=True, blank=True)
    productuser = models.CharField(max_length=20, default='user')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.productuser} sold {self.productname} to {self.sold_to}.'


class Sold_out(models.Model):
    sold_to = models.CharField(max_length=20, default='user')
    product = models.CharField(max_length=20, default='product')
    productname = models.CharField(max_length=50, default='product')
    productcategory = models.CharField(max_length=50, default='product')
    productprice = models.IntegerField(default=0)
    productimg = models.ImageField(upload_to='pics', null=True, blank=True)
    productuser = models.CharField(max_length=20, default='user')
    timestamp = models.DateTimeField(auto_now_add=True)


class Updates(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Testimony(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=250, default='OK')
    timestamp = models.DateTimeField(auto_now_add=True)


class LookingFor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
