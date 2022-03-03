from django.db import models

class imageInfo(models.Model):
    imagePath = models.CharField(max_length=200, null=False, blank=False)
    res = models.CharField(max_length=50, null=False, blank=False)
