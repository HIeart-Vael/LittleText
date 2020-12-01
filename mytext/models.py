from django.db import models

from login.models import User


class Record(models.Model):
    # User为外键
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(null=True)
    place = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=1000)
