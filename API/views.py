from django.shortcuts import render, redirect
from pytube import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']
        video = YouTube(link)

        stream = video.streams.get_lowest_resolution()

        stream.download()

        return render(request, 'API/youtube.html')
    return render(request, 'API/youtube.html')



