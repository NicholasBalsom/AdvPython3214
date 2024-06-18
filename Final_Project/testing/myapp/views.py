import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube

from .forms import DownloadForm


def download_view(request):
    if request.method == "POST":
        form = DownloadForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data["video_url"]
            yt = YouTube(video_url)
            video_title = yt.title
            stream = yt.streams.filter(only_audio=True).first()
            mp3_filename = f"{video_title}.mp3"
            stream.download(filename=mp3_filename, output_path="tmp")
            return render(request, "myapp/download.html", {"mp3_filename": mp3_filename})
    else:
        form = DownloadForm()
    return render(request, "myapp/index.html", {"form": form})


def download_mp3(request, mp3_filename):
    mp3_path = os.path.join(settings.MEDIA_ROOT, "tmp", mp3_filename)
    if os.path.exists(mp3_path):
        with open(mp3_path, "rb") as mp3_file:
            response = HttpResponse(mp3_file.read(), content_type="audio/mpeg")
            response["Content-Disposition"] = 'attachment; filename="{}"'.format(mp3_filename)
            return response
    else:
        return HttpResponse("MP3 file not found", status=404)
