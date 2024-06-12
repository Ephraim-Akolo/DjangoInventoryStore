from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListcreateInventoryItems.as_view(), name='list-create-inventory'),
    path('<uuid:pk>/', views.RetrieveUpdateDestroyInventoryItems.as_view(), name='retrieve-update-inventory'),
]