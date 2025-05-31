from django.db import models




class Crane(models.Model):
    name = models.CharField(verbose_name="نام")
    slug = models.SlugField(verbose_name="اسلاگ", unique=True)

    image = models.FileField(verbose_name="تصویر", upload_to="Cranes/images/")

    conetnt = models.TextField(verbose_name="محتوا", null=True, blank=True)


    class Meta:
        verbose_name = "جرثقیل"
        verbose_name_plural = "جرثقیل ها"

    
    def __str__(self):
        return self.name