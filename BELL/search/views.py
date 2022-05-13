from django.shortcuts import render
from sellitem.models import ListItem


# Create your views here.
def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items = ListItem.objects.filter(itemname__icontains=searched)
        return render(request, 'search/index.html', {'searched': searched, 'items': items})
    else:
        return render(request, 'search/index.html', {})



