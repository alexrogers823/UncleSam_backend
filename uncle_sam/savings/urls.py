from django.urls import path
from savings import views

urlpatterns = [
    path('', views.SavingList.as_view()),
    path('<int:pk>/', views.SavingDetail.as_view())
]