from django.shortcuts import render
from sellitem.models import get_specific_item


def get_itemdetails(itemid):
    return get_specific_item(itemid)


def index(request, itemid):
    return render(request, 'itemdetails/index.html', context={'itemdetails': get_itemdetails(itemid)})

