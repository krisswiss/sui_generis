from django.db import models

# Create your models here.


class Social(models.Model):
    name = models.CharField(max_length=50)
    weblink = models.URLField()
    icon = models.CharField(max_length=20)
    def __str__(self):
        return self.question
