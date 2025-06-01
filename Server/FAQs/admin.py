from django.contrib import admin
from .models import Faq



@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']
    search_fields = ['question', 'answer']
