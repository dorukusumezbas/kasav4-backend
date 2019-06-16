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
    bank = models.ManyToManyField('self', related_name='receiver_banks', symmetrical=False)

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
    transaction_method = models.CharField(max_length= 30, null= True)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.SET_NULL, null= True)
    bank = models.ForeignKey(Bank, on_delete= models.SET_NULL, null= True)
    bank_from = models.ForeignKey(Bank, on_delete= models.SET_NULL, null= True, related_name='bank_from')
    bank_to = models.ForeignKey(Bank, on_delete= models.SET_NULL, null= True, related_name='bank_to')

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        transaction = super(Transaction, self).save(*args, **kwargs)
        #checks if transaction is an entry transaction
        if str(getattr(self, 'transaction_type')) == "Giriş":
            if getattr(self, 'transaction_method') == 'cash':
                nakit_kasa = Bank.objects.get(pk=1)
                current_balance = nakit_kasa.balance
                nakit_kasa.balance = current_balance + getattr(self, 'amount')
                nakit_kasa.save()
            elif getattr(self, 'transaction_method') == 'bank':
                print(getattr(self, 'bank'))
                banka = Bank.objects.filter(title= getattr(self, 'bank')).first()
                current_balance = banka.balance
                banka.balance = current_balance + getattr(self, 'amount')
                banka.save()
        elif str(getattr(self, 'transaction_type')) == "Çıkış":
            if getattr(self, 'transaction_method') == 'cash':
                nakit_kasa = Bank.objects.get(pk=1)
                current_balance = nakit_kasa.balance
                nakit_kasa.balance = current_balance + getattr(self, 'amount')
                nakit_kasa.save()
            elif getattr(self, 'transaction_method') == 'bank':
                print(getattr(self, 'bank'))
                banka = Bank.objects.filter(title= getattr(self, 'bank')).first()
                current_balance = banka.balance
                banka.balance = current_balance - getattr(self, 'amount')
                banka.save()
        elif str(getattr(self, 'transaction_type')) == "Virman":
            bank_from =Bank.objects.filter(title = getattr(self, 'bank_from')).first()
            bank_to = Bank.objects.filter(title=getattr(self, 'bank_to')).first()
            bank_from.balance = bank_from.balance - getattr(self, 'amount')
            bank_to.balance = bank_to.balance + getattr(self, 'amount')
            bank_from.save()
            bank_to.save()

        #add check and credit card functionality
        return transaction

