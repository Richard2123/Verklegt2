from django.shortcuts import render
from .models import get_your_bids

# Create your views here.


def index(request):
    current_user = request.user
    return render(request, 'yourbids/index.html', context={'yourbids': get_your_bids(current_user)})
