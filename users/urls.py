from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig

from .views import UserRegisterCreateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:product_list"), name="logout"),
    path("register/", UserRegisterCreateView.as_view(), name="register"),
]
