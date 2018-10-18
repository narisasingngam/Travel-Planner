from django.db import models

class SearchMap(models.Model):
    location = models.CharField(max_length = 30)
    time = models.IntegerField(null=True)
