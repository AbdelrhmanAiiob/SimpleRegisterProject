from django.shortcuts import render, redirect
from .forms import CustomCreationUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# sign_in_page
def sign_in(request):
  
  if request.method == 'POST':
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user_info = authenticate(
      request,
      username=username,
      password=password
    )
  
    if user_info is not None:
      login(request, user_info)
      return redirect('index')
    else:
      messages.info(
        request,
        'Username OR Password Is Incorrect.'
      )
      return render(request, 'accounts/sign_in.html')
  
  return render(request, 'accounts/sign_in.html')

# sign_up_page
def sign_up(request):
    
    if request.method == 'POST':
    
      form = CustomCreationUserForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        messages.success(
          request,
          'Registration Successful.'
          )
        return redirect('sign_in')
      
      # List Actual Errors. 
      else:
        for field, errors in form.errors.items():
          for error in errors :
            messages.error(request, error.title())
    
    # Not 'POST'
    else:
      form= CustomCreationUserForm()
    
    return render(request, 'accounts/sign_up.html', {'form':form})

# log_out
def log_out(request):
  logout(request)
  return render(request, 'accounts/sign_in.html')

# error_404_page
def error_404(request):
    return render(request, '404.html')






















