from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
