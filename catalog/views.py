from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.models import Product

from .forms import ProductForm


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/product_contacts.html"
