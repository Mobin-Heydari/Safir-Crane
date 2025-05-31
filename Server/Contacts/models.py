from django.db import models





class Contact(models.Model):
    # Define status options for managing inquiry progress
    class ContactStatusChoices(models.TextChoices):
        NEW = 'NEW', 'جدید'
        IN_PROGRESS = 'INP', 'درحال برسی'
        COMPLETED = 'COM', 'برسی شده'
        ARCHIVED = 'ARC', 'بایگانی شده'


    # Basic contact fields
    title = models.CharField(verbose_name="عنوان", max_length=255)

    content = models.TextField(verbose_name="محتوا")

    f_name = models.CharField(verbose_name="نام", max_length=255)

    l_name = models.CharField(verbose_name="نام خانوادگی", max_length=255)

    phone = models.CharField(verbose_name="شماره تماس", max_length=255, blank=True)

    email = models.EmailField(verbose_name="ایمیل")

    # Workflow and metadata fields
    status = models.CharField(
        max_length=3, 
        choices=ContactStatusChoices.choices, 
        default=ContactStatusChoices.NEW,
    )

    # Read and ignore flags for interface management
    is_ignored = models.BooleanField(default=True)
    is_readed = models.BooleanField(default=False)


    # Timestamps for record keeping
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'تماس فوری'
        verbose_name_plural = 'تماس های فوری'
        ordering = ['-created_at']  # Most recent contacts first
    

    def __str__(self):
        return f"{self.title} - {self.name}"