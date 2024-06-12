from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListcreateSuppliers.as_view(), name='list-create-suppliers'),
    path('<uuid:pk>/', views.RetrieveUpdateSuppliers.as_view(), name='retrieve-update-suppliers'),
]