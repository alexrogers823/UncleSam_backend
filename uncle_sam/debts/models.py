from django.db import models


class Debt(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['title']
