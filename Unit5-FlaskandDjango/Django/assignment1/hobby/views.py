from django.http import HttpResponse
from django.shortcuts import render


def hobby_info_view(request):
    text = """I enjoy downhill skiing because I like the thrill of flying 
    through the air, doing flips, tricks and whatever you can think of. 
    I enjoy most adrenaline sports and downhill skiing is one of them."""

    return HttpResponse(
        f"<html><body style='text-align: center;'><h1>Downhill Skiing</h1>\n<h2 style='margin: auto; width: 50%;'>{text}</h2></body></html>"
    )


def hobby_image_view(request):
    url = "https://skicanadamag.com/wp-content/uploads/2019/02/marblemountian.dkp-145_CMYK.jpg"
    alt_text = "Downhill skiing at Marble Mountain, Stedy Brook, NL"

    return HttpResponse(f"<img src={url} alt={alt_text} height=100% style='display: block; margin: auto;'>")
