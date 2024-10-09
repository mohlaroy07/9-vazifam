from django.urls import path

from .views import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("add_ad/", add_ad, name="add_page")
]
