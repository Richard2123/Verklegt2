from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        items =
        return render(request, 'search/index.html', {'searched': searched})
    else:
        return render(request, 'search/index.html')

