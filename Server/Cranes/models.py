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
    


class CraneContent(models.Model):

    crane = models.ForeignKey(
        Crane,
        on_delete=models.CASCADE,
        verbose_name="جرثقیل",
        related_name="crane_contents"
    )

    title = models.CharField(
        verbose_name="عنوان", 
        blank=True, null=True
    )

    content = models.TextField(
        verbose_name="محتوا",
        blank=True, null=True
    )

    image = models.FileField(
        upload_to="Cranes/Content/images/",
        verbose_name="تصویر",
        null=True, blank=True
    )


    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا ها"

    
    def __str__(self):
        return f'{self.title}--{self.crane.name}'