from django.contrib import admin

from .models import Reference, Toner, Consumption, Customer, Direction, ReleaseVoucher
# Register your models here.

admin.site.register(Reference)
admin.site.register(Toner)
admin.site.register(Direction)
admin.site.register(Customer)
admin.site.register(Consumption)
admin.site.register(ReleaseVoucher)