from django.db import models




class Category(models.Model):
    name = models.CharField(verbose_name="نام", max_length=255)
    slug = models.SlugField(verbose_name="اسلاگ", max_length=255, unique=True)

    image = models.ImageField(upload_to="Blogs/Category/images/")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    
    def __str__(self):
        return self.name



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
    