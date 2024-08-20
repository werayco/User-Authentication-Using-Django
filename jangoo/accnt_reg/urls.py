from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/",views.signer,name="sign"),
    path("log-in/",views.loginer,name="login"),
    path("log-out/",views.logouter,name="logout"),
]