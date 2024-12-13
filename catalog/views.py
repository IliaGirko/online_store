from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView, TemplateView, DetailView
from django.urls import reverse_lazy
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product



class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    fields = ["name", "description", "price", "image", "category",]


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    fields = ["name", "description", "price", "image", "category",]


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/product_contacts.html"


# def home(request):
#     context = {"products": Product.objects.all()}
#     return render(request, "product_list.html", context)
#
#
# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         return HttpResponse(f"{name} спасибо, за обращение. Мы свяжемся с Вами в ближайшее время.")
#     return render(request, "product_contacts.html")
#
#
# def get_product(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {"product": product}
#     return render(request, "product_detail.html", context)
