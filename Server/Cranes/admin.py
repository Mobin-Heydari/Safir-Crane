from django.contrib import admin
from .models import Crane, CraneContent, CraneImages, CraneRequest





# Inline editing for CraneContent
class CraneContentInline(admin.TabularInline):
    model = CraneContent
    extra = 1
    fields = ['title', 'content', 'image']
    verbose_name = "محتوا"
    verbose_name_plural = "محتواها"



# Inline editing for CraneImages
class CraneImagesInline(admin.TabularInline):
    model = CraneImages
    extra = 1
    fields = ['image']
    verbose_name = "تصویر"
    verbose_name_plural = "تصاویر"



@admin.register(Crane)
class CraneAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'views', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CraneContentInline, CraneImagesInline]
    fieldsets = (
        ("محتوای کلی", {
            "fields": ('name', 'slug', 'image', 'content', 'views')
        }),
        ("تاریخ ها", {
            "fields": ('created_at', 'updated_at'),
            "classes": ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')



@admin.register(CraneContent)
class CraneContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'crane', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'crane__name']
    list_filter = ['crane']
    readonly_fields = ('created_at', 'updated_at')



@admin.register(CraneImages)
class CraneImagesAdmin(admin.ModelAdmin):
    list_display = ['crane', 'created_at', 'updated_at']
    search_fields = ['crane__name']
    list_filter = ['crane']
    readonly_fields = ('created_at', 'updated_at')



@admin.register(CraneRequest)
class CraneRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'f_name', 'l_name', 'phone', 'email', 'status', 'is_readed', 'is_ignored', 'created_at']
    search_fields = ['title', 'f_name', 'l_name', 'content', 'email']
    list_filter = ['status', 'is_readed', 'is_ignored']
    readonly_fields = ('created_at', 'updated_at')
