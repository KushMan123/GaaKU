from django.contrib import admin
from .models import Profile, Notification, History, Updates, Testimony, Sold_out, LookingFor

# Register your models here.
admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(History)
admin.site.register(Updates)
admin.site.register(Testimony)
admin.site.register(Sold_out)
admin.site.register(LookingFor)
