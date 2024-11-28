from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"{name} спасибо, за обращение. Мы свяжемся с Вами в ближайшее время.")
    return render(request, "contacts.html")
