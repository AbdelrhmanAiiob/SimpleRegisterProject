from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('emailsignup', views.sign_up, name='sign_up'),
    path('404', views.error_404, name='404'),
]

