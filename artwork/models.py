from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
import uuid

#this will be the user directory, all images will be uploaded for the user. basically file uploading with django
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', default = 'default.png') #verbose name is human readable name
    art_name = models.CharField(max_length=255, default=0)
    caption = models.CharField(max_length=1000000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


    # def get_absolute_url(self): #the url of that specific artwork post
    #     return reverse('post-details', args=[str(self.id)])
    
    def __str__(self):
        return str(self.id)
    



    