from django.urls import path
from . import views

urlpatterns = [
    path('aboutus', views.about_us, name='aboutus'),
    path('profile', views.my_profile, name='profile'),
    path('', views.index, name='index'),
]