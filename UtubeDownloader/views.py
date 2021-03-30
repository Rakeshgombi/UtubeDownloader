from django.shortcuts import render
from pytube import YouTube


def index(request):
    if request.method == 'POST':
        url = request.POST.get('ytUrl', '')
        return (url)
    return render(request, "index.html")


def search(request):
    url = index(request)
    try:
        yt = YouTube(url)
        vidStreams = yt.streams.filter(progressive=True)
        title = yt.title
        audStreams = yt.streams.filter(only_audio=True)
        thank = True
        return render(
            request, "search.html", {
                "vidStreams": vidStreams,
                'audStreams': audStreams,
                'url': url,
                'title': title,
                'thank': thank
            })
    except:
        thank = False
        return render(request, "search.html", {"thank": thank})
