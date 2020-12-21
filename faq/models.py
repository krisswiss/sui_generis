from django.db import models

# Create your models here.


class faq(models.Model):
    question = models.CharField(max_length=254)
    answer = models.TextField()
    def __str__(self):
        return self.question
