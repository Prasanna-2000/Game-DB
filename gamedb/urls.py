from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("gamepage", views.gamepage, name="gamepage"),
    path("<int:game_id>", views.mainpage, name="mainpage"),
    path("logout", views.logout, name="logout")
] 