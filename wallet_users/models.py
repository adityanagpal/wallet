from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    govt_id = models.CharField(max_length=150, unique=True)

class Wallet(models.Model):
    name = models.CharField(max_length=100,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # balance = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    transaction_time = models.DateTimeField(default=datetime.now())

    def clean(self):
        super().clean()
        if self.debit == 0 and self.credit == 0:
            raise 'Field1 or field2 are both Zero'
