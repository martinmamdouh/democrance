from django.contrib import admin
from customer.models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Customer, CustomerAdmin)
