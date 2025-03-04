from archives import views
from django.urls import path

urlpatterns = [
    path('', views.ArchiveList.as_view()),
    path('charts/', views.ArchiveChartList.as_view())
]