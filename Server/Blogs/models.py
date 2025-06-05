from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(verbose_name="نام", max_length=255)
    slug = models.SlugField(verbose_name="اسلاگ", max_length=255, unique=True)

    image = models.ImageField(upload_to="Blogs/Category/images/")

    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")

    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blogs:blog-detail", kwargs={"slug": self.slug})
    



class Blog(models.Model):

    class BlogStatus(models.TextChoices):
        DRAFT = "D", "تکمیل نشده"
        PUBLISHED = "P", "منتشر شده"

    
    title = models.CharField(verbose_name="عنوان", max_length=255)
    slug = models.SlugField(verbose_name="اسلاگ", max_length=255, unique=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="دسته بندی",
        related_name="category_blogs"
    )

    content = models.TextField(verbose_name="محتوا")

    views = models.IntegerField(verbose_name="تعداد بازدید", default=0)

    status = models.CharField(
        verbose_name="وضعیت",
        max_length=3,
        choices=BlogStatus.choices,
        default=BlogStatus.DRAFT
    )

    image = models.ImageField(verbose_name="تصویر", upload_to="Blogs/images/")

    published_date = models.DateField(verbose_name="تاریخ انتشار", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="تاریخ آپدیت", auto_now=True)

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'

    def __str__(self):
        return self.title
    

class BlogContent(models.Model):
    blog = models.ForeignKey(
        Blog,
        verbose_name="بلاگ",
        on_delete=models.CASCADE,
        related_name='blog_contents'
    )

    title = models.CharField(
        verbose_name="عنوان",
        max_length=255,
        blank=True, null=True
    )

    content = models.TextField(verbose_name="محتوا", null=True, blank=True)

    image = models.ImageField(verbose_name="تصویر", upload_to="Blogs/content/images/", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="تاریخ آپدیت", auto_now=True)

    class Meta:
        verbose_name = 'محتوای بلاگ'
        verbose_name_plural = 'محتوا های بلاگ ها'

    def __str__(self):
        return f'{self.blog.title}'
    


class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog,
        verbose_name="بلاگ",
        on_delete=models.CASCADE,
        related_name='blog_comments'
    )

    name = models.CharField(verbose_name="نام و نام خانوادگی", max_length=50)

    content = models.TextField(verbose_name="محتوا")

    created_at = models.DateTimeField(verbose_name="تاریخ ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="تاریخ آپدیت", auto_now=True)

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'{self.blog.title}'