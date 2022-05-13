from django.shortcuts import render
from BELL.forms import SellItemForm


# Create your views here.
def index(request):
    return render(request, 'sellitem/test.html')

def sell_item(request):
    if request.method == 'POST':
        form = SellItemForm(data=request.POST)
        instance = form.save(commit=False)
        instance.user = request.user
        form.save()
    return render(request, 'sellitem/test.html', {'form': SellItemForm()})

    # Return a new untouched form
