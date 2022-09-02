from statistics import mode
from django.db import models

# Create your models here.
class Edit(models.Model):
    img = models.ImageField(upload_to='media')
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"