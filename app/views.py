from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Customers


# Method Create
class CustomerCreateView(CreateView):
    model = Customers
    fields = '__all__'
    template_name = 'customer_form.html'
    success_url = 'customers'


# Method List
class CustomerListView(ListView):
    model = Customers
    template_name = 'customer_list.html'


class CustomerDetailView(DetailView):
    model = Customers
    template_name = 'customer_list_id.html'
    context_object_name = 'customer'


# Method Update
class CustomerUpdateView(UpdateView):
    model = Customers
    fields = '__all__'
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customers_list')


# Method Delete
class CustomerDeleteView(DeleteView):
    model = Customers
    template_name = 'customers_confirm_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customers_list')
