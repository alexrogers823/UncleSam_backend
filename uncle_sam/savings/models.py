from django.db import models


class Saving(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=150)
    current_amount = models.DecimalField(max_digits=8, decimal_places=2)
    priority = models.PositiveSmallIntegerField(default=1)
    goal = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    goal_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['priority']
