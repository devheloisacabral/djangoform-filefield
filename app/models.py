from django.db import models

# Create your models here.
class modelfield(models.Model):
    title = models.CharField(max_length=20)
    doc = models.FileField(upload_to='doc')

    def __str__(self) -> str:
        return self.title