from django.db import models
from django.urls import reverse




class Crane(models.Model):
    name = models.CharField(verbose_name="نام")
    slug = models.SlugField(verbose_name="اسلاگ", unique=True)

    image = models.FileField(verbose_name="تصویر", upload_to="Cranes/images/")

    content = models.TextField(verbose_name="محتوا", null=True, blank=True)

    views = models.IntegerField(verbose_name="تعداد بازدید", default=0)

    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")


    class Meta:
        verbose_name = "جرثقیل"
        verbose_name_plural = "جرثقیل ها"

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("cranes:crane-detail", kwargs={"slug": self.slug})
    
    


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

    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")


    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا ها"

    
    def __str__(self):
        return f'{self.title}--{self.crane.name}'



class CraneImages(models.Model):

    crane = models.ForeignKey(
        Crane,
        on_delete=models.CASCADE,
        verbose_name="جرثقیل",
        related_name="crane_images"
    )

    image = models.FileField(
        upload_to="Cranes/Images/images/",
        verbose_name="تصویر",
        null=True, blank=True
    )

    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")


    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"

    
    def __str__(self):
        return f'{self.crane.name}'
    


class CraneRequest(models.Model):

    # Define status options for managing inquiry progress
    class RequestStatusChoices(models.TextChoices):
        NEW = 'N', 'جدید'
        PENDING = 'P', 'درحال برسی'
        COMPLETED = 'C', 'تکمیل شده'
        ARCHIVED = 'A', 'بایگانی شده'
        VERIFIED = 'V', 'تایید شده'
        REJECTED = 'R', 'رد شده'


    crane = models.ForeignKey(
        Crane,
        on_delete=models.CASCADE,
        verbose_name="جرثقیل",
        related_name="crane_requests"
    )

    # Basic request fields
    title = models.CharField(verbose_name="عنوان", max_length=255)

    content = models.TextField(verbose_name="محتوا")

    f_name = models.CharField(verbose_name="نام", max_length=255)

    l_name = models.CharField(verbose_name="نام خانوادگی", max_length=255)

    phone = models.CharField(verbose_name="شماره تماس", max_length=255, blank=True)

    email = models.EmailField(verbose_name="ایمیل")

    # Workflow and metadata fields
    status = models.CharField(
        max_length=3, 
        choices=RequestStatusChoices.choices, 
        default=RequestStatusChoices.NEW,
        verbose_name="وضعیت درخواست"
    )

    # Read and ignore flags for interface management
    is_ignored = models.BooleanField(default=True, verbose_name="نادیده گرفته شده؟")
    is_readed = models.BooleanField(default=False, verbose_name="خوانده شده؟")


    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آپدیت")


    class Meta:
        verbose_name = 'درخواست'
        verbose_name_plural = 'درخواست ها'
        ordering = ['-created_at']  # Most recent contacts first
    

    def __str__(self):
        return f"{self.title} - {self.crane.name}"
