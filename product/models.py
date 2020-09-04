from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    like = models.ManyToManyField(User , blank=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.name

