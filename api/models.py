from django.db import models

# Create your models here.
class Transaction(models.Model):
    operation = models.CharField(max_length=10)
    amount = models.FloatField()
    currency = models.CharField(max_length=10)
    rate = models.FloatField()
    total = models.FloatField()
    username = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)