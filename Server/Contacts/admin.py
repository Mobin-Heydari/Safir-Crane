from django.contrib import admin
from .models import Contact




@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'f_name', 
        'l_name', 
        'phone', 
        'email', 
        'status', 
        'is_readed', 
        'is_ignored', 
        'created_at'
    )
    list_filter = ('status', 'is_readed', 'is_ignored', 'created_at')
    search_fields = ('title', 'content', 'f_name', 'l_name', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')
