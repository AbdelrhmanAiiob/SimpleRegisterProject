from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def about_us(request):
    return render(request, 'pages/about_us.html')

@login_required(login_url='sign_in')
def my_profile(request):
    return render(request, 'pages/my_profile.html')


@login_required(login_url='sign_in')
def index(request):
    return render(request, 'pages/index.html')