from django import forms

from .models import Post

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
        model = Post
        fields = [
            "title",
            "content",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({"class": "form-control", "placeholder": "Введите заголовок"})

        self.fields["content"].widget.attrs.update({"class": "form-control", "placeholder": "Введите контент"})

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )
