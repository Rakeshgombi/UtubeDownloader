import pafy
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        url = request.POST.get('ytUrl', '')
        return (url)
    return render(request, "index.html")


def search(request):
    url = index(request)
    video = pafy.new(url)
    title = video.title
    vidStreams = video.streams
    audStreams = video.audiostreams
    return render(request, "search.html", {"vidStreams": vidStreams, 'audStreams': audStreams, 'url': url, 'title': title})
