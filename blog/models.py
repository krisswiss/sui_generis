from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=254)
    introduction = models.CharField(max_length=254)
    post = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
