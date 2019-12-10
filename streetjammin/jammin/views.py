from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Musicians, Songs, Downloads, SongUploadForm
# from .models import Musician << this is how we import models

# Create your views here.
def index(request):
    # musician = Musician.objects.create(mid = 3, username = "bob") <<<< this is a test (it works)
    return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})

def login(request):
    return render(request, 'basic_templates/registration/login')

def signup(request):
    return render(request, 'basic_templates/registration/signup')

def upload(request):
  if request.method == 'POST':
    form = SongUploadForm(request.POST, request.FILES)
    if form.is_valid():

      song_name = form.cleaned_data['name']
      song_address = 'jammin/media/' + song_name + '.mp3'
      with open(song_address, 'wb+' ) as destination:
        for chunk in request.FILES['song_file'].chunks():
          destination.write(chunk)
        song = Songs.objects.create(mid=321, sid=456, name=song_name, song_file=song_address)
        return HttpResponseRedirect('/')
  else:
    form = SongUploadForm()
  return render(request, 'basic_templates/upload.html', {'form': form})
