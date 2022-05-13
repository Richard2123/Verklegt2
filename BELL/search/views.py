from django.shortcuts import render
from sellitem.models import ListItem


# Create your views here.
def index(request):
    if request.method == "POST":
        items_list = []
        searched = request.POST['searched']
        sorting = request.POST['sorting']
        if sorting == 'name':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('itemname')
            for i in items:
                if not i.sold:
                    items_list.append(i)
            return render(request, 'search/index.html', {'searched': searched, 'items': items_list})
        elif sorting == 'lower-price':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('base_price')
            for i in items:
                if not i.sold:
                    items_list.append(i)
            return render(request, 'search/index.html', {'searched': searched, 'items': items_list})
        elif sorting == 'higher-price':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('-base_price')
            for i in items:
                if not i.sold:
                    items_list.append(i)
            return render(request, 'search/index.html', {'searched': searched, 'items': items_list})
    else:
        return render(request, 'search/index.html', {})



