import os
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import Songs, Musicians, Downloads, SongUploadForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
# from .models import Musician << this is how we import models

# Create your views here.
def index(request):
    return mySongs(request)
def login(request):
    return render(request, 'basic_templates/registration/login')

def signup(request):
    return render(request, 'basic_templates/registration/signup')

def uploadSongs(request):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        if request.method == 'POST':
            form = SongUploadForm(request.POST, request.FILES)
            if form.is_valid():
              song_name = form.cleaned_data['name']
              song_address = 'jammin/media/' + song_name + '.mp3'
              with open(song_address, 'wb+' ) as destination:
                for chunk in request.FILES['song_file'].chunks():
                  destination.write(chunk)
                song = Songs.objects.create(mid=request.user.id, name=song_name, song_file=song_address)
                return HttpResponseRedirect('/list')
        else:
            form = SongUploadForm()
            return render(request, 'basic_templates/uploads.html', {'form': form})

def mySongs(request):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        data = Songs.objects.filter(mid=request.user.id)

        list = {
            "songs": data
        }
        return render(request, 'basic_templates/list.html', list)

def logout_view(request):
    logout(request)
    return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})

def qrcode(request, sid):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        song = Songs.objects.get(sid=sid)
        download = Downloads.objects.create(sid=song.sid, mid=song.mid)
        download_uri = request.build_absolute_uri('/download/' + str(download.did) + '/')

        return render(request, 'basic_templates/qrcode.html', { "song": song, "download_uri": download_uri })

def download(request, did):
    download = Downloads.objects.filter(did=did).first()
    if download is None:
        raise Http404
    if download.downloaded_or_not():
        return HttpResponse("Sorry, this song has already been downloaded.")
    song = Songs.objects.get(sid=download.sid)
    with song.song_file.open() as file_download:
        response = HttpResponse(file_download.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = 'attachment; filename=' + song.name + ".mp3"
        download.state = True
        download.save(force_update=True)
        return response
    raise Http404
