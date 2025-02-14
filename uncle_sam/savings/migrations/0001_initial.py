# Generated by Django 5.1.6 on 2025-02-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('current_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('goal', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('goal_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['priority'],
            },
        ),
    ]
