from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    limit = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    ignore = models.BooleanField(default=False)

    def __str__(self):
        return self.description
