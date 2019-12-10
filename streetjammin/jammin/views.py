from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Musicians, Songs, Downloads, SongUploadForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Anonymous views
#################
def index(request):
    # musician = Musician.objects.create(mid = 3, username = "bob") <<<< this is a test (it works)
  if request.user.is_authenticated():
    return home(request)
  else:
    return anon_home(request)


def anon_home(request):
  return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})

def login(request):
  return render(request, 'basic_templates/registration/login')
    #TO DO
    # after login, automatically redirected to musicianpage, which contains
          # an upload button
          # a list of songs you uploaded, along with num of downloads (downloaded =True) so far, and
          # a create_dl_objects button where you specify num of dl objects to create

def signup(request):
    # return render(request, 'basic_templates/registration/signup')
  if request.method == 'POST':
    form = MyUserCreationForm(request.POST)
    new_user = form.save(commit=True)
    # Create a mirror sharded User model.
    u = Profile(
        user_id=new_user.id, username=new_user.username, 
        first_name=new_user.first_name, last_name=new_user.last_name)
    u.save()
    # Log in that user.
    user = authenticate(username=new_user.username,
                        password=form.clean_password2())
    if user is not None:
      login(request, user)
    else:
      raise Exception
    return home(request)
  else:
    form = MyUserCreationForm
  return render(request, 'micro/register.html', {'form' : form})



# Authenticated views
####################
@login_required
def home(request):
  #list of songs you've uploaded & metrics
  my_songs = Songs.objects.filter(mid =request.user.id).order_by('created')

@login_required
def upload(request): #this should only be accessible after you login (shouldn't be accessible at landing page)
  if request.method == 'POST':
    form = SongUploadForm(request.POST, request.FILES)
    if form.is_valid():

      song_name = form.cleaned_data['name']
      song_address = 'jammin/media/' + song_name + '.mp3'
      with open(song_address, 'wb+' ) as destination:
        for chunk in request.FILES['song_file'].chunks():
          destination.write(chunk)
        song = Songs.objects.create(mid=321, name=song_name, song_file=song_address) #if we only allow musicians who HAVE LOGGED IN ALREADY to arrive at this feature (upload), then we can get this specific musician's mid and put it here in the mid field.
                                                                                      #TO DO: find out how to get the mid field of this specific musician
        return HttpResponseRedirect('/')
  else:
    form = SongUploadForm()
  return render(request, 'basic_templates/musician/upload.html', {'form': form})



