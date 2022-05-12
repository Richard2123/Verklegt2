from django.shortcuts import render, redirect
from BELL.forms import SellItemForm


# Create your views here.
def index(request):
    return render(request, 'sellitem/test.html')


def post_item(request):
    if request.method == 'POST':
        print(1)
    return render(request, 'sellitem/test.html', {'form': SellItemForm()})


