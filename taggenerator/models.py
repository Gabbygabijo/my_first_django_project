from django.db import models

# Create your models here.

class Tag(models.Model):
    input = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.input