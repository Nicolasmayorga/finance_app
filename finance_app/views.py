from django.db.models import Sum
from rest_framework import generics, filters
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TransactionListCreate(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BudgetCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=over_budget']

    def get_queryset(self):
        queryset = super().get_queryset()
        categories = []

        for category in queryset:
            total_transactions = Transaction.objects.filter(
                category=category).aggregate(
                Sum('amount'))['amount__sum'] or 0
            over_budget = total_transactions > category.limit
            setattr(category, "over_budget", over_budget)
            categories.append(category)

        return categories
