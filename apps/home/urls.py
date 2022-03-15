from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from apps.home import views
from apps.home.views import login_view, register_user

urlpatterns = [

    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
