from django.shortcuts import render
from sellitem.models import ListItem


# Create your views here.
def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        sorting = request.POST['sorting']
        if sorting == 'name':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('itemname')
            return render(request, 'search/index.html', {'searched': searched, 'items': items})
        elif sorting == 'lower-price':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('base_price')
            return render(request, 'search/index.html', {'searched': searched, 'items': items})
        elif sorting == 'higher-price':
            items = ListItem.objects.filter(itemname__icontains=searched).order_by('-base_price')
            return render(request, 'search/index.html', {'searched': searched, 'items': items})
    else:
        return render(request, 'search/index.html', {})



