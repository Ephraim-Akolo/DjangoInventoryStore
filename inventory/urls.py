from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListcreateInventoryItems.as_view()),
    path('<uuid:pk>/', views.RetrieveUpdateDestroyInventoryItems.as_view()),
]