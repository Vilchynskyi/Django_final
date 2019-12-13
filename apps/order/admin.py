from django.contrib import admin
from .models import Order, OrderBook


class OrderBookInline(admin.TabularInline):
    model = OrderBook
    extra = 0
    fields = ('book', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'created_at', 'complete')
    list_display_links = ('id', 'email', 'phone', 'created_at')
    search_fields = ('id', 'email', 'phone')
    list_editable = ('complete',)
    list_filter = ('complete',)

    inlines = (OrderBookInline,)

