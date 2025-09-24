# Simple Register Page. (Hints)=> First Time Write **'Markdown'**

  ## The Start Data.

  ### Templates :-
  * accounts
    * sign_in.html
    * sign_up.html

  * pages
    * about_us.html
    * index.html
    * my_profile.html

  * parts
    * navbar.html
    * footer.html

  * 404.html
  * parent.html

  ### The First Steps :-
  > 
    Definition => templates, static, media ✅
    Apps%urls.py ✅
    Bundlle The Templates With Nav, Foot, {% url 'name' %} ✅
  > 

  ## Sign_up, Sign_in And Sign_out
  ### Sign_up :- __Before Start Should Know Which Form_Way Gonna Use__
  >
  Forms_Way: **'UserCreationForm'** & Built-in **'User'** Form Wich Import The Data From 'User' Built-in Form
  >

  ## *If Not Gonna Create New Fields*
  ### Create forms.py
    ```py

    from django import forms
    from django.contrib.auth.models import User
    from django.contrib.auth.forms import UserCreationForm

    class UserCreateFrom(UserCreationForm):
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2', 'email']
    ```

  ### In views.py
    ```py

    from .forms import UserCreateFrom

    if request.method == 'POST':
      form = UserCreateFrom
      if form.is_valid():
        form.save()

        return render({'form':form})
    ```

  ## If Wanna Create New Fields
  ### In models.py 
  #### Add Fields Into 'User'
>
          # Add New Fields.
          ## from django.contrib.auth.models import Abstractuser
          ## from django.db import models
>

  ## Create New Fields
    ```py
          class CustomUser(AbstractUser):

            phone_number = models.CharField(
              max_length=15,
              blank=True,
              null=True
              )

            images = models.ImageField(
              upload_to='images/%y/%m/%d',
              default='static/navbar/images/profile.jpg'
            )

            def __str__(self):
              return self.username
    ```

  ## Create forms.py
    ```py
            # Import The Used Modules #

              # Use Form.
                ## from django import form

              # Use UserCreationForm.
                ## from django.contrib.auth.forms import UserCreationForm

              # Use 'User' Built-in Form.
                ## from django.contrib.auth.models import User
    ```

  ## Creation Form
    ```py
              class CustomUserCreationForm(UserCreationForm):
                class Meta:
                  model = CustomUser
                  fields = [
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'phone_number',
                    'images'
                    ]
    ```

  ## After Finish The Custom 'USER'
  >
    In MainProject settings.py.
    Undr INSTALLED_APPS.
    AUTH_USER_MODEL = 'appName.CustomModelName'
    For No Issue del db, migrations AppName And migrate
  >

  ## If CustomUser You Need To Added Into ADMIN PANEL
    ```py
      from .models import CustomUser
      admin.site.register(CustomUser)
    ```

  ## If Wanna Your Forms Have The Same Design In Bootstrap
  ### In forms.py
      ```py
          # After MetaClass
          def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)

            self.fields['fieldName'].widget.attrs.update(
              'class' : 'form-control',
              'placeholder' : 'MSG'
            )
      ```

  ## Loop On Tehm
    ```py
        for field_name, field in self.fields.items():
          field.widget.attrs['class'] = 'form-control'
    ```

  ## To Make A Field Required
    ```py
          self.field.required = True
    ```

  ## In viwes.py
      ```py
        # To Show The Actual Error!, If The for.is_not_valid().
          # for field, errors in form.errors.item():
            for error in errors:
              messages.error(
                request,
                f"{field.capitalize()}:{error}" #Dont Use 'field' Here Just Custom The Errors (ADVANCED)
              )
      ```

  ## Sign_in :-
  # Import The Used Modules.
      ```py
        from django.contrib.auth import authenticate, login, logout

        if request.method == 'POST':

          # Get Used Login Info
          username = request.POST.get('username')
          password = request.POST.get('password')

          user_auth = authenticate(
            request,
            username=username,
            password=password
          )

          # Sure The User Coming Info In Database.
          if user_auth is not None
            login(request, user_auth)
            return redirct('index')

          else:
            messages.info(
              request,
              'Username OR Password Is Incorrect.'
            )
            return render(request, 'sign_in')
      ```

  ## Sign_out :-
    #Simple Knowledge.

## log_out
    ```py
      def log_out(request):
        logout(request)
        return render(request, 'accounts/sign_in.html')

      2- from django.contrib.auth.decorators import login_required

    <!-- Then Go To Any viewPage -->
    @login_required(login_url='sign_in')
    ```
