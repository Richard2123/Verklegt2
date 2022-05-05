from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'search/index.html', {'searched': searched})
    else:
        return render(request, 'search/index.html')

