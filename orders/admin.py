from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','email', 'address', 'phone_number', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated',]
    inlines = [OrderItemInline]
    search_fields = ('email','phone_number','paid','name')
    list_editable = ['paid']
    list_display_links = ['id','email','name',]


admin.site.register(Order, OrderAdmin)



