from django.db import models
from django.urls import reverse
from django.contrib import messages


class Categories(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('more', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


