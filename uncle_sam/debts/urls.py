from debts import views
from django.urls import path

urlpatterns = [
    path('debts/', views.debt_list),
    path('debts/<int:pk>/', views.debt_detail)
]