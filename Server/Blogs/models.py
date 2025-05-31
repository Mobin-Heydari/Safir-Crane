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
