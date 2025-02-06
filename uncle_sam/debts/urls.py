from debts import views
from django.urls import path

urlpatterns = [
    path('', views.DebtList.as_view()),
    path('<int:pk>/', views.DebtDetail.as_view())
]