from django.shortcuts import render
from BELL.forms import CheckoutForm

# Create your views here.


def index(request):
    context = {'form': CheckoutForm}
    return render(request, 'checkout/index.html', context)


