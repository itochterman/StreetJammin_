from django.shortcuts import render
# from .models import Musician << this is how we import models 

# Create your views here.
def index(request):
    # musician = Musician.objects.create(mid = 3, username = "bob") <<<< this is a test (it works)
    return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})

def login(request):
    return render(request, 'basic_templates/registration/login')

def signup(request):
    return render(request, 'basic_templates/registration/signup')