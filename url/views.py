from django.shortcuts import render, redirect, get_object_or_404
from .models import UrlData
import hashlib


def index(request):
    short_url = ""
    if request.method == "POST":
        original_url = request.POST.get("original_url")

        existing = UrlData.objects.filter(original_url=original_url).first()
        if existing:
            short_code = existing.short_code
        else:
            h = hashlib.shake_256(original_url.encode())
            short_code = h.hexdigest(5)

            while UrlData.objects.filter(short_code=short_code).exists():
                original_url += "x"  # tweak input slightly
                h = hashlib.shake_256(original_url.encode())
                short_code = h.hexdigest(5)

            UrlData.objects.create(original_url=original_url, short_code=short_code)

        short_url = request.build_absolute_uri(f"/{short_code}/")

    return render(request, 'index.html', {'short_url': short_url})


def redirect_url(request, code):
    url_obj = get_object_or_404(UrlData, short_code=code)
    return redirect(url_obj.original_url)
