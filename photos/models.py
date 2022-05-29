from django.db import models
import os
from datetime import datetime

# rename photo upon upload
def photo_rename(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    upload_time = datetime.now()
    return 'images/wedding_davis/{now}{ext}'.format(now = upload_time, ext = file_extension)

# Create your models here.
class Photo(models.Model):
    img = models.ImageField(upload_to=photo_rename)
    caption = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return str(self.caption)
