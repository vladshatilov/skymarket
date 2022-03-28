from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    title = models.CharField(max_length=512, blank=False)
    price = models.PositiveIntegerField(blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True, max_length=4096)


class Comment(models.Model):
    text = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, blank=True, null=True)
