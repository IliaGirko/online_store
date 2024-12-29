from django.core.cache import cache

from config.settings import CACHE_ENABLED

from .models import Product


class ProductByCatalog:

    @staticmethod
    def get_products_by_category(category_id):
        if not CACHE_ENABLED:
            return Product.objects.filter(category_id=category_id)
        key = f"products_by_category_{category_id}"
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products, 60)
        return products

    @staticmethod
    def get_queryset_product_list():
        cache_product_list = cache.get("product_list")

        if cache_product_list:
            return cache_product_list

        queryset = Product.objects.all()
        cache.set("product_list", queryset, 60)
        return queryset
