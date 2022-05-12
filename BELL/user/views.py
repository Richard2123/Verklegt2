from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile
from BELL.forms import EditProfileForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
        })


def index(request):
    return render(request, 'user/register.html')


def edit_profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = EditProfileForm(instance=Profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/userprofile')
    return render(request, 'edituserprofile/index.html', {
        'form': EditProfileForm(instance=profile)
    })