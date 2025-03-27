from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='categories', null=True, blank=True)

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='services', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)




    def __str__(self):
        return self.title
