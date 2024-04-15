from django.urls import path

from . import views

urlpatterns = [
    path("", views.hobby_info_view, name="hobby_info"),
    path("image/", views.hobby_image_view, name="hobby_image"),
]
