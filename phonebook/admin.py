from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email']
    ordering = ['first_name', 'last_name']
