from debts import views
from django.urls import path

urlpatterns = [
    path('debts/', views.DebtList.as_view()),
    path('debts/<int:pk>/', views.DebtDetail.as_view())
]