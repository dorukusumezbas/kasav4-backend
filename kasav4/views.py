from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from rest_framework import generics
from rest_framework import filters
from url_filter.integrations.drf import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000


class CurrencyView(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TableView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TableSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_fields = "__all__"
    ordering_fields = '__all__'
    ordering = ('-datetime')
    pagination_class = StandardResultsSetPagination


class OneView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        one_query = One.objects.filter(transaction_type=body["transaction_type"]).values()
        return JsonResponse({
            "success": True,
            "content": list(one_query)
        })


class FilterTransactionTypeView(APIView):
    def post(self, request):
        query = TransactionType.objects.all().values()
        return JsonResponse({
            "success": True,
            "content": list(query)
        })


class FilterOneView(APIView):
    def post(self, request):
        query = One.objects.all().values()
        return JsonResponse({
            "success": True,
            "content": list(query)
        })


class CategoriesView(APIView):
    def post(self, request):
        content_array = []
        body = json.loads(request.body)
        two_query = Two.objects.filter(upper_category=body["id"])
        for index1, item1 in enumerate(two_query):
            content_array.append({
                "value": item1.id,
                "label": item1.title,
                "children": []
                 })
            three_query = Three.objects.filter(upper_category= item1.id)
            for index2, item2 in enumerate(three_query):
                content_array[index1]["children"].append({
                    "value": item2.id,
                    "label": item2.title,
                    "children": []
                     })
                four_query = Four.objects.filter(upper_category=item2.id)
                for index3, item3 in enumerate(four_query):
                    content_array[index1]["children"][index2]["children"].append({
                        "value": item3.id,
                        "label": item3.title,
                    })
        return JsonResponse({
            "success": True,
            "content": content_array
        })


class BankView(viewsets.ModelViewSet):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()