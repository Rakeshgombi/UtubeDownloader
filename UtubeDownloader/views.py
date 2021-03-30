import pafy
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        url = request.POST.get('ytUrl', '')
        return (url)
    return render(request, "index.html")


def search(request):
    url = index(request)
    try:
        video = pafy.new(url)
        title = video.title
        vidStreams = video.streams
        audStreams = video.audiostreams
        thank = True
        return render(request, "search.html", {"vidStreams": vidStreams, 'audStreams': audStreams, 'url': url, 'title': title, 'thank': thank})
    except:
        thank = False
        return render(request, "search.html", {"thank": thank})