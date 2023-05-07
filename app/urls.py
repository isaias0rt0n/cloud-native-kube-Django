from django.urls import path, include
from .views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDetailView, CustomerDeleteView

urlpatterns = [
    path('signup', CustomerCreateView.as_view()),
    path('customers', CustomerListView.as_view(), name='customers_list'),
    path('signup/<int:pk>', CustomerUpdateView.as_view(), name='customer_form'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer_list'),
    path('customer_delete/<int:pk>', CustomerDeleteView.as_view(), name='customer_delete')
]
