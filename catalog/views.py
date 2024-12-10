from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category

def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"{name} спасибо, за обращение. Мы свяжемся с Вами в ближайшее время.")
    return render(request, "contacts.html")


def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product.html", context)

