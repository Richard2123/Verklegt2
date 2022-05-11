from django.shortcuts import render
from edituserprofile.models import EditProfile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'userprofile/index.html')