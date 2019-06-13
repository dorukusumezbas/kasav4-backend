from django.db import models


class TransactionType(models.Model):
    title = models.CharField(max_length= 60)

    def __str__(self):
        return self.title


class One(models.Model):
    title = models.CharField(max_length= 60)
    transaction_type = models.ForeignKey(TransactionType, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


class Two(models.Model):
    title = models.CharField(max_length= 60)
    upper_category = models.ForeignKey(One, on_delete= models.CASCADE)

    def __str__(self):
        return self.title


class Three(models.Model):
    title = models.CharField(max_length= 60)
    upper_category = models.ForeignKey(Two, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Four(models.Model):
    title = models.CharField(max_length= 60)
    upper_category = models.ForeignKey(Three, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Currency(models.Model):
    title = models.CharField(max_length= 60)

    def __str__(self):
        return self.title


class Bank(models.Model):
    title = models.CharField(max_length=60)
    isBank = models.BooleanField()
    balance = models.IntegerField()


    def __str__(self):
        return self.title


class Transaction(models.Model):
    description = models.CharField(max_length=60)
    amount = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now=False)
    one = models.ForeignKey(One, on_delete=models.SET_NULL, null= True)
    two = models.ForeignKey(Two, on_delete=models.SET_NULL, null=True)
    three = models.ForeignKey(Three, on_delete=models.SET_NULL, null=True)
    four = models.ForeignKey(Four, on_delete=models.SET_NULL, null=True)
    transaction_method = models.CharField(max_length= 30)
    transaction_type = models.CharField(max_length=10)
    bank = models.ForeignKey(Bank, on_delete= models.SET_NULL, null= True)

    def __str__(self):
        return self.description

