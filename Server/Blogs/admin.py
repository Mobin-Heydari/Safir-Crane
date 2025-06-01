from django.contrib import admin
from .models import Category, Blog, BlogContent, BlogComment





# Inline editing for BlogContent within a Blog entry
class BlogContentInline(admin.TabularInline):
    model = BlogContent
    extra = 1
    fields = ['title', 'content', 'image']
    verbose_name = "محتوای بلاگ"
    verbose_name_plural = "محتوا های بلاگ"



# Inline editing for BlogComment allowing you to review comments associated with a Blog
class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 1
    fields = ['content', 'created_at', 'updated_at']
    verbose_name = "کامنت"
    verbose_name_plural = "کامنت ها"
    readonly_fields = ['created_at', 'updated_at']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'views', 'published_date', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['status', 'category']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    inlines = [BlogContentInline, BlogCommentInline]



@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['blog']
    readonly_fields = ['created_at', 'updated_at']



@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'created_at', 'updated_at']
    search_fields = ['content', 'blog__title']
    list_filter = ['blog']
    readonly_fields = ['created_at', 'updated_at']
