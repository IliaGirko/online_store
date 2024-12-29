from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Category, Product
from .services import ProductByCatalog


class ProductsByCategoryView(ListView):
    template_name = "catalog/select_product_list.html"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return ProductByCatalog.get_products_by_category(category_id=category_id)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return ProductByCatalog.get_queryset_product_list()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = Category.objects.all()
        return context


@method_decorator(cache_page(60), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        user = request.user
        count: int = 0
        print(product.owner)
        if product.owner != user:
            count += 1
        if not request.user.has_perm("catalog.can_unpublish_product"):
            count += 1
        if count > 1:
            return HttpResponseForbidden("У Вас нет права отменять публикацию")
        # elif not :
        #     return HttpResponseForbidden("У Вас нет права отменять публикацию")
        product.is_active = False
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    form_class = ProductForm

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner == user or user.has_perm("catalog.can_unpublish_product"):
            return product

        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner == user or user.has_perm("catalog.can_unpublish_product"):
            return product

        raise PermissionDenied


class ProductTemplateView(TemplateView):
    model = Product
    template_name = "catalog/product_contacts.html"
