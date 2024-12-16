from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    fields = [
        "name",
        "description",
        "price",
        "image",
        "category",
    ]


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    fields = [
        "name",
        "description",
        "price",
        "image",
        "category",
    ]


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/product_contacts.html"
