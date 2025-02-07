from django.db import models


# Create your models here.
class Item(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    completed = models.BooleanField(default=False)
    url_link = models.URLField(max_length=300, blank=True, null=True)

    class Meta:
        ordering = ['created']
