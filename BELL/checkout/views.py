from django.shortcuts import render
from BELL.forms import CheckoutForm
from sellitem.models import ListItem
# Create your views here.

#No matter how much I tried I could not get this to upload to the databasepip
def index(request, item_id):
    item = ListItem.objects.get(id=item_id)
    context = {'form': CheckoutForm}
    if request.method == 'POST':
        print(request.POST)
        checkout = CheckoutForm(data=request.POST)
        checkout.user_id = request.user.id
        checkout.item_id = item.id
        if checkout.is_valid():
            checkout.save()
    return render(request, 'checkout/index.html', context)


