from django.db import models




class Faq(models.Model):
    question = models.TextField(verbose_name="سوال")
    answer = models.TextField(verbose_name="جواب")

    class Meta:
        verbose_name = "سوال متداول"
        verbose_name_plural = "سوال های متداول"

    def __str__(self):
        return self.question[:30]