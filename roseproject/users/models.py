from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        mywidth = 300
        img = Image.open(self.image.path)
        width, height = img.size
        print(width)
        ratio = width/height
        wpercent = (mywidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((mywidth,hsize), Image.ANTIALIAS) 
        output_size = (mywidth,hsize)
        img.thumbnail(output_size)
        img.save(self.image.path)