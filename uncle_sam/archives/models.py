from django.db import models


class Archive(models.Model):
    type = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    title = models.CharField(max_length=100)
    updated_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'updated_date']