from django.db import models
import os
from datetime import datetime
# image compression
from io import BytesIO  #basic input/output operation
from PIL import Image #Imported to compress images
from django.core.files import File #to store files

#image compression method
# def compress(image):
#     im = Image.open(image)
#     if im.mode != 'RGB':
#         im = im.convert('RGB')
#     im_io = BytesIO()
#     im.save(im_io, 'JPEG', quality=60)
#     new_image = File(im_io, name=image.name)
#     return new_image

# rename photo upon upload
def photo_rename(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    upload_time = datetime.now()
    upload_time = upload_time.strftime("%Y-%m-%d %H:%M")
    return 'images/wedding_davis/{now}{ext}'.format(now = upload_time, ext = file_extension)

# Create your models here.
class Photo(models.Model):
    img = models.ImageField(upload_to=photo_rename)
    caption = models.CharField(max_length=75, blank=True)
    date =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)

    # #calling image compression function before saving the data
    # def save(self, *args, **kwargs):
    #     new_image =  compress(self.img)
    #     self.img = new_image
    #     super().save(*args, **kwargs)
