from django.db import models
from django.utils import timezone

# Create your models here.
class MyBlog(models.Model):
    title = models.TextField(max_length=30)
    desc = models.TextField(max_length=20000)
    cre_date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.title