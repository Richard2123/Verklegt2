from django.shortcuts import render, redirect
from BELL.forms import SellItemForm


# Create your views here.
def index(request):
    return render(request, 'sellitem/test.html')


def post_item(request):
    if request.method == 'POST':
        form = SellItemForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'sellitem/test.html')

    return render(request, 'sellitem/test.html', {'form': SellItemForm()})
