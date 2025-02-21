from django.contrib import admin
from .models import ServiceQuote

@admin.register(ServiceQuote)
class ServiceQuoteAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'price', 'created_at')
