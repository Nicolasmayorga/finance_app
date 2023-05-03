from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Transaction


class CategoryTests(APITestCase):

    def test_create_category(self):
        url = reverse('category_list_create')
        data = {'name': 'Test Category', 'limit': 1000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_list_categories(self):
        Category.objects.create(name='Test Category', limit=1000)
        url = reverse('category_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_category(self):
        category = Category.objects.create(name='Test Category', limit=1000)
        url = reverse('category_retrieve_update_destroy', kwargs={'pk': category.id})
        data = {'name': 'Test Category Updated', 'limit': 2000}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'Test Category Updated')
        self.assertEqual(Category.objects.get().limit, 2000)

    def test_delete_category(self):
        category = Category.objects.create(name='Test Category', limit=1000)
        url = reverse('category_retrieve_update_destroy', kwargs={'pk': category.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


class TransactionTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', limit=1000)

    def test_create_transaction(self):
        url = reverse('transaction_list_create')
        data = {
            'description': 'Test Transaction',
            'category': self.category.id,
            'amount': 200,
            'date': '2023-04-26',
            'ignore': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.get().description, 'Test Transaction')

    def test_list_transactions(self):
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        url = reverse('transaction_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_transaction(self):
        transaction = Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        url = reverse('transaction_retrieve_update_destroy', kwargs={'pk': transaction.id})
        data = {
            'description': 'Test Transaction Updated',
            'category': self.category.id,
            'amount': 400,
            'date': '2023-04-26',
            'ignore': False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Transaction.objects.get().description, 'Test Transaction Updated')
        self.assertEqual(Transaction.objects.get().amount, 400)

    def test_delete_transaction(self):
        transaction = Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        url = reverse('transaction_retrieve_update_destroy', kwargs={'pk': transaction.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Transaction.objects.count(), 0)


class BudgetCategoriesTests(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', limit=1000)

    def test_budget_categories(self):
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        url = reverse('budget_categories')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_budget_categories_with_multiple_transactions(self):
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        url = reverse('budget_categories')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_budget_categories_with_multiple_categories(self):
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        category2 = Category.objects.create(name='Test Category 2', limit=1000)
        Transaction.objects.create(description='Test Transaction', category=category2, amount=200, date='2023-04-26')
        url = reverse('budget_categories')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_budget_categories_with_multiple_transactions_and_categories(self):
        Transaction.objects.create(
            description='Test Transaction',
            category=self.category,
            amount=200,
            date='2023-04-26')
        category2 = Category.objects.create(name='Test Category 2', limit=1000)
        Transaction.objects.create(description='Test Transaction', category=category2, amount=200, date='2023-04-26')
        Transaction.objects.create(description='Test Transaction', category=category2, amount=200, date='2023-04-26')
        url = reverse('budget_categories')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
