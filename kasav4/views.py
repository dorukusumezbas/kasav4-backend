from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.core import serializers
import json
import logging

class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class OneView(APIView):
    def get(self, request):
        one_query = One.objects.all().values()
        return JsonResponse({
            "success": True,
            "content": list(one_query)
        })


class TwoView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        two_query = Two.objects.filter(upper_category= body["id"]).values()
        return JsonResponse({
            "success": True,
            "content": list(two_query)
        })

class ThreeView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        two_query = Three.objects.filter(upper_category= body["id"]).values()
        return JsonResponse({
            "success": True,
            "content": list(two_query)
        })

class FourView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        two_query = Four.objects.filter(upper_category= body["id"]).values()
        return JsonResponse({
            "success": True,
            "content": list(two_query)
        })

class FiveView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        two_query = Five.objects.filter(upper_category= body["id"]).values()
        return JsonResponse({
            "success": True,
            "content": list(two_query)
        })

