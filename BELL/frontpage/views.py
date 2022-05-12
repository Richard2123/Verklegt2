from django.shortcuts import render
from sellitem.models import get_frontpage_listings



"""frontpage_suggested = [
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'},
    {'image': 'https://d27jswm5an3efw.cloudfront.net/app/uploads/2019/07/insert-image-html.jpg', 'name': 'something',
     'rating': 'unknown', 'highest': '10'}
]"""


def get_frontpage():
    return get_frontpage_listings()


def index(request):
    return render(request, 'frontpage/index.html', context={'frontpage_suggested': frontpage_suggested})


frontpage_suggested = get_frontpage()

