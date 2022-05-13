from django.shortcuts import render
from sellitem.models import ListItem


"""def get_itemdetails(item_id=0):
    return get_specific_item(item_id)"""


def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    return render(request, 'itemdetails/index.html', context={'itemdetails': item})

