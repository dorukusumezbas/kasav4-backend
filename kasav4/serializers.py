from rest_framework import serializers
from .models import *


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionType
        fields = "__all__"


class OneSerializer(serializers.ModelSerializer):
    class Meta:
        model = One
        fields = "__all__"


class TwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Two
        fields = "__all__"


class ThreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Three
        fields = "__all__"


class FourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Four
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = "__all__"