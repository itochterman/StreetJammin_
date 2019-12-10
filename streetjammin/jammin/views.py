from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from .models import Songs
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
        return render(request, 'basic_templates/uploads.html')

def mySongs(request):
    if not request.user.is_authenticated:
        return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})
    else:
        data = Songs.objects.all()

        list = {
            "songs": data
        }
        return render(request, 'basic_templates/list.html', list)
