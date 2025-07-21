from django.db import models
from django.utils import timezone

class Data(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    money = models.IntegerField()
    date = models.DateTimeField(default=timezone.localtime())

    def __str__(self):
        return self.name

