from django.shortcuts import render
from sellitem.models import ListItem
from BELL.forms import MakeBid


def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    form = MakeBid()
    if request.method == 'POST':
        bid = request.POST['bid']
        print(bid)
        bid = int(bid)
        highest_bid = item.highest_bid
        highest_bid = int(highest_bid)
        if bid > highest_bid:
            print('test')
            bidform = MakeBid(data=request.POST)
            instance = bidform.save(commit=False)
            instance.bidder_id = request.user.id
            instance.item_id = item.id
            item.highest_bid = bid
            item.save()
            bidform.save()
        else:
            pass

    return render(request, 'itemdetails/index.html', context={'item': item, 'form': form})

