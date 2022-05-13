from django.shortcuts import render
from sellitem.models import get_your_items
from sellitem.models import ListItem

# Create your views here.


def get_items(user):
    return get_your_items(user)


def index(request):
    current_user = request.user
    item = ListItem
    return render(request, 'youritems/index.html', context={'your_items': get_items(current_user)})




