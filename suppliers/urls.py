from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListcreateSupplierItems.as_view()),
    path('<uuid:pk>/', views.RetrieveUpdateInventoryItems.as_view()),
]