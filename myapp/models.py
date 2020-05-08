from django.db import models

# Create your models here.
class PYnews(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    publisher = models.CharField(max_length=100)
    content = models.TextField()
    link = models.CharField(max_length=100)


class Comments(models.Model):
    posted_by = models.TextField(max_length=1000)

    comment = models.TextField(max_length=100)

    article = models.IntegerField()

    create_time = models.DateField(auto_now_add=True)