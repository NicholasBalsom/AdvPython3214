from django.urls import path

from . import views

urlpatterns = [
    path("", views.download_view, name="download_view"),
    path("download/<str:mp3_filename>/", views.download_mp3, name="download_mp3"),
]
