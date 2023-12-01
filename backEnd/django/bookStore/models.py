from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=255)
    pub_year
