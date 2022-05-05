from django.shortcuts import render

frontpage_suggested = [
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
]


def index(request):
    return render(request, 'frontpage/index.html', context={'frontpage_suggested': frontpage_suggested})
