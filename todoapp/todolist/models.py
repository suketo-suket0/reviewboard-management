from django.db import models

# Create your models here.

class todo(models.Model):
    content = models.TextField()