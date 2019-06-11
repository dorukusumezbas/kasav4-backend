from django.db import models


class One(models.Model):
    title = models.CharField(max_length= 60)

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


class Five(models.Model):
    title = models.CharField(max_length= 60)
    upper_category = models.ForeignKey(Four, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Currency(models.Model):
    title = models.CharField(max_length= 60)


TRANSACTION_METHODS = (
    ("cash", "Nakit"),
    ("bank", "Banka"),
    ("check", "Çek"),
    ("credit_card", "Kredi Kartı"),
)


class Transaction(models.Model):
    description = models.CharField(max_length=60)
    amount = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now=False)
    one = models.ForeignKey(One, on_delete=models.SET_NULL, null= True)
    two = models.ForeignKey(Two, on_delete=models.SET_NULL, null=True)
    three = models.ForeignKey(Three, on_delete=models.SET_NULL, null=True)
    four = models.ForeignKey(Four, on_delete=models.SET_NULL, null=True)
    five = models.ForeignKey(Five, on_delete=models.SET_NULL, null=True)
    transaction_method = models.CharField(max_length= 30, choices=TRANSACTION_METHODS)

