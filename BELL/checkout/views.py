from django.shortcuts import render
from BELL.forms import CheckoutForm
from sellitem.models import ListItem
# Create your views here.


def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    context = {'form': CheckoutForm}
    if request.method == 'POST':
        print(request.POST)
        checkout = CheckoutForm(data=request.POST)
        instance = checkout.save(commit=False)
        instance.user = request.user.id
        instance.item = item_id
        instance.rating = 2
        checkout.save()
    return render(request, 'checkout/index.html', context)


