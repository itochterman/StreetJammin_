from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import Songs, Musicians, Downloads, SongUploadForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db.models import FileField
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
                song = Songs.objects.create(mid=717, name=song_name, song_file=song_address)
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

def qrcode(request, sid):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        song = Songs.objects.get(sid=sid)
        download = Downloads.objects.create(sid=song.sid, mid=song.mid)
        download_uri = request.build_absolute_uri('/download/' + str(download.did) + '/')

        return render(request, 'basic_templates/qrcode.html', { "song": song, "download_uri": download_uri })

def file_cleanup(sender, **kwargs):
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
            if field and isinstance(field, FileField):
                inst = kwargs['instance']
                f = getattr(inst, fieldname)
                m = inst.__class__._default_manager
                if hasattr(f, 'path') and os.path.exists(f.path)\
                and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
                .exclude(pk=inst._get_pk_val()):
                try:
                    default_storage.delete(f.path)
                except:
                    pass
