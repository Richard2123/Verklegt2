from django.shortcuts import render
from sellitem.models import ListItem



def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    print(item)
    return render(request, 'youritemdetail/index.html', context={'item': item})