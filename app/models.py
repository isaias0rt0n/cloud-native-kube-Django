from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    date_birth = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    job = models.CharField(max_length=100, null=False, blank=False)
