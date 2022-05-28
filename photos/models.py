from django.db import models

# Create your models here.
class Photo(models.Model):
    img = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=75)

    def __str__(self):
        return str(self.caption)
