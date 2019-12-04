from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'basic_templates/index.html', {'title': "StreetJammin", 'contributors': "By Yumi, Alice, Jamie and Bella"})

def login(request):
    return render(request, 'basic_templates/registration/login')