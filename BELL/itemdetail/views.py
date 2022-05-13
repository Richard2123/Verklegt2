from django.shortcuts import render
from sellitem.models import ListItem
from BELL.forms import MakeBid

"""def get_itemdetails(item_id=0):
    return get_specific_item(item_id)"""


def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    form = MakeBid
    if request.method == 'POST':
        print(request.POST['bid'])
        bid = request.POST['bid']
        if bid > item.highest_bid:
            item.highest_bid = bid
            item.save()
        else:
            pass

    return render(request, 'itemdetails/index.html', context={'item': item, 'form': form})

