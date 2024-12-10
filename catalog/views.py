from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {"products": Product.objects.all()}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"{name} спасибо, за обращение. Мы свяжемся с Вами в ближайшее время.")
    return render(request, "contacts.html")


def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "get_product.html", context)
