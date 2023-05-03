from django.urls import path
from . import views

urlpatterns = [
    path(
        'categories/',
        views.CategoryListCreate.as_view(),
        name='category_list_create'),
    path(
        'categories/<int:pk>/',
        views.CategoryRetrieveUpdateDestroy.as_view(),
        name='category_retrieve_update_destroy'),
    path(
        'transactions/',
        views.TransactionListCreate.as_view(),
        name='transaction_list_create'),
    path(
        'transactions/<int:pk>/',
        views.TransactionRetrieveUpdateDestroy.as_view(),
        name='transaction_retrieve_update_destroy'),
    path(
        'budget_categories/',
        views.BudgetCategories.as_view(),
        name='budget_categories'),
]
