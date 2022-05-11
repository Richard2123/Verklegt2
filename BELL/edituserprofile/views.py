from django.shortcuts import render, redirect
from BELL.forms import EditProfileForm

# Create your views here.
def index(request):
    submitted = False
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/edituserprofile?submitted=True')
    else:
        form = EditProfileForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'edituserprofile/index.html', {'form': form, 'submitted': submitted})

