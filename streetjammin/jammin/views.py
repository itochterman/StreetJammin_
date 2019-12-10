from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import Songs, Musicians, Downloads, SongUploadForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# from .models import Musician << this is how we import models

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # musician = Musician.objects.create(mid = 3, username = "bob") <<<< this is a test (it works)
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        data = Songs.objects.all()

        list = {
            "songs": data
        }
        return render(request, 'basic_templates/list.html', list)
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
                song = Songs.objects.create(mid=765, sid=456, name=song_name, song_file=song_address)
                return HttpResponseRedirect('/list')
        else:
            form = SongUploadForm()
            return render(request, 'basic_templates/uploads.html', {'form': form})

def mySongs(request):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        data = Songs.objects.all()

        list = {
            "songs": data
        }
        return render(request, 'basic_templates/list.html', list)

def logout_view(request):
    logout(request)
    return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
