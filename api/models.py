from django.db import models

class Transaction(models.Model):
    OPERATION_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    operation = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.amount * self.rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.operation} - {self.amount} {self.currency}"
