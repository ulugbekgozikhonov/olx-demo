from django.urls import path
from .views import register, login, home, logout, verify_view

app_name = 'users'


urlpatterns = [
    path("register/", register, name="register"),
    # path("login/", login, name="login"),
    path("login/", login, name="login"),
    path("home/", home, name="home"),
    path("logout/", logout, name="logout"),
    path("verify/", verify_view, name="verify"),    

]
