from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="signup"),
    path(
        "signin/",
        LoginView.as_view(
            template_name="users/signin.html",
            form_class=LoginForm,
            redirect_authenticated_user=True,
            success_url="/",
        ),
        name="signin",
    ),
    path("logout/", LogoutView.as_view(next_page="quotes:root"), name="logout"),
]
