from django.shortcuts import render, redirect
from BELL.forms import SellItemForm


# Create your views here.
def index(request):
    return render(request, 'sellitem/test.html')

def sell_item(request):
    if request.method == 'POST':
        form = SellItemForm(data=request.POST)
        form.save()
    return render(request, 'sellitem/test.html', {'form': SellItemForm()})

    # Return a new untouched form
