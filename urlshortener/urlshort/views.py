from django.shortcuts import render, redirect
from .models import URL
from .utils import generate_short_url


def home(request):
    urls = URL.objects.all()
    return render(request, 'urlshort/home.html', {'urls': urls})


def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '').strip()
        if long_url:
            url, created = URL.objects.get_or_create(
                long_url=long_url,
                defaults={'short_url': generate_short_url()}
            )
            if created:
                while URL.objects.filter(short_url=url.short_url).exclude(pk=url.pk).exists():
                    url.short_url = generate_short_url()
                    url.save(update_fields=['short_url'])
            return redirect('home')
    return render(request, 'urlshort/shorten_url.html')


def redirect_to_original(request, short_url):
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.long_url)
    except URL.DoesNotExist:
        return render(request, 'urlshort/not_found.html', {'short_url': short_url}, status=404)
