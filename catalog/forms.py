from django import forms
from django.core.exceptions import ValidationError

from .models import Product

list_of_banned_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите название продукта"})

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание продукта"}
        )

        self.fields["price"].widget.attrs.update({"class": "form-control", "placeholder": "Укажите стоимость"})

        self.fields["image"].widget.attrs.update({"class": "form-control", "placeholder": "Добавьте изображение"})

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        result: int = 0
        for word in list_of_banned_words:
            if word in name.lower():
                result += 1
        if result > 0:
            raise ValidationError("В названии продукта запрещенные слово/а")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        result: int = 0
        for word in list_of_banned_words:
            if word in description.lower():
                result += 1
        if result > 0:
            raise ValidationError("В описании продукта запрещенные слово/а")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Стоимость продукта не может быть 0 или меньше 0")
        return price
