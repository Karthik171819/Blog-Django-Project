from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

#category
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#remeber after creating model please make sure migrate it
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.ImageField(null=True, upload_to= "posts/images") #change the field from Url to ImageField to upload image
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title

#dynamic content for about_us page
class AboutUs(models.Model):
    content = models.TextField()

    # def __str__(self):
    #     return self.content

    
