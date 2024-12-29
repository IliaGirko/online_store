from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("product_list/", views.ProductListView.as_view(), name="product_list"),
    path("select_product_list/<int:category_id>/", views.ProductsByCategoryView.as_view(), name="select_product_list"),
    path("product_list/<int:pk>/detail/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product_list/create", views.ProductCreateView.as_view(), name="product_form"),
    path("product_list/<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("product_list/<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", views.ProductTemplateView.as_view(), name="product_contacts"),
]
