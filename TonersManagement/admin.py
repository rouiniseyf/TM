from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Toner)
admin.site.register(Direction)
admin.site.register(Customer)
admin.site.register(Consumption)
admin.site.register(ReleaseVoucher)
admin.site.register(Offer)
admin.site.register(Simcard)
admin.site.register(Hardware)  