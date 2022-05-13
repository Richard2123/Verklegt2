from django.shortcuts import render
from sellitem.models import get_frontpage_listings


def get_frontpage():
    return get_frontpage_listings()


def index(request):
    return render(request, 'frontpage/index.html', context={'frontpage_suggested': frontpage_suggested})


frontpage_suggested = get_frontpage()

