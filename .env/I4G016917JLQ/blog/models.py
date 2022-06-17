from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class post(models.Model):
    Title = models.CharField(max_length=200, null=True, blank=True, default='')
    Text = models.TextField(null=True, blank=True, default='')
    Author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=''
        )
    Created_date = models.DateTimeField(default=datetime.now())
    Published_date = models.DateTimeField(default=datetime.now())