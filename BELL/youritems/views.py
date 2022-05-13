from django.shortcuts import render
from sellitem.models import get_your_items

# Create your views here.

def get_items():
    return get_your_items()


def index(request):
    return render(request, 'youritems/index.html', context={'your_items': your_items})


your_items = get_items()



