from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "country",
            "phone_number",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите Email"})

        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Введите username"})

        self.fields["country"].widget.attrs.update({"class": "form-control", "placeholder": "Укажите Вашу страну"})

        self.fields["phone_number"].widget.attrs.update({"class": "form-control", "placeholder": "Укажите телефон"})

        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Введите пароль"})

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль еще раз"}
        )
