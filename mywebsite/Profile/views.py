from django.shortcuts import render
from .models import Profile, Resume

def profile(request):
    profile = Profile.objects.first()
    return render(request, 'profile/profile.html', {'profile': profile})

def resume(request):
    resume = Resume.objects.all()
    return render(request, 'profile/resume.html', {'resume': resume})