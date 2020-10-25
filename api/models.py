from django.db import models


class seodata(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class urlindex(models.Model):
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
